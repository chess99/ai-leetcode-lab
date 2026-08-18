from __future__ import annotations

import ast
import re
from typing import Any


def _issue(
    slug: str, kind: str, message: str, line: int | None = None
) -> dict[str, Any]:
    result: dict[str, Any] = {"slug": slug, "kind": kind, "message": message}
    if line is not None:
        result["line"] = line
    return result


def _python_tree(source: str) -> ast.Module | None:
    try:
        return ast.parse(source)
    except SyntaxError:
        # Syntax validation reports this separately.
        return None


def _python_hash_table_issue(
    slug: str, source: str, *, structure: str
) -> dict[str, Any] | None:
    tree = _python_tree(source)
    if tree is None:
        return None
    forbidden_calls = {"set", "frozenset", "dict", "defaultdict", "Counter", "OrderedDict"}
    for node in ast.walk(tree):
        if isinstance(node, (ast.Set, ast.SetComp, ast.Dict, ast.DictComp)):
            return _issue(
                slug,
                "restriction_violation_builtin_hash_table",
                f"{structure} 不得使用 Python set/dict 作为底层结构",
                getattr(node, "lineno", None),
            )
        if not isinstance(node, ast.Call):
            continue
        name = (
            node.func.id
            if isinstance(node.func, ast.Name)
            else node.func.attr
            if isinstance(node.func, ast.Attribute)
            else ""
        )
        if name in forbidden_calls:
            return _issue(
                slug,
                "restriction_violation_builtin_hash_table",
                f"{structure} 不得调用内建哈希表结构 {name}()",
                getattr(node, "lineno", None),
            )
    return None


def candidate_restriction_issues(
    title_slug: str, language: str, source: str
) -> list[dict[str, Any]]:
    """Return source-level violations for restrictions enforced by LeetCode.

    These checks intentionally target restrictions stated by the archived problem
    and observed in the remote judge. They supplement syntax/interface checks and
    run before candidate registration or any remote action.
    """
    slug = str(title_slug)
    issues: list[dict[str, Any]] = []

    if slug == "sum-of-two-integers" and language == "python3":
        tree = _python_tree(source)
        if tree is not None:
            forbidden = (ast.Add, ast.Sub, ast.UAdd, ast.USub)
            for node in ast.walk(tree):
                operator: ast.AST | None = None
                if isinstance(node, (ast.BinOp, ast.UnaryOp, ast.AugAssign)):
                    operator = node.op
                if isinstance(operator, forbidden):
                    issues.append(
                        _issue(
                            slug,
                            "restriction_violation_add_subtract_operator",
                            "371 两整数之和不得使用 + 或 - 运算符",
                            getattr(node, "lineno", None),
                        )
                    )
                    break

    elif slug == "design-hashset" and language == "python3":
        issue = _python_hash_table_issue(slug, source, structure="705 设计哈希集合")
        if issue is not None:
            issues.append(issue)

    elif slug == "design-hashmap" and language == "python3":
        issue = _python_hash_table_issue(slug, source, structure="706 设计哈希映射")
        if issue is not None:
            issues.append(issue)

    elif slug == "sort-an-array" and language == "python3":
        tree = _python_tree(source)
        if tree is not None:
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                is_sorted = isinstance(node.func, ast.Name) and node.func.id == "sorted"
                is_sort_method = isinstance(node.func, ast.Attribute) and node.func.attr == "sort"
                if is_sorted or is_sort_method:
                    issues.append(
                        _issue(
                            slug,
                            "restriction_violation_builtin_sort",
                            "912 排序数组不得使用 sorted() 或 .sort() 内置排序",
                            getattr(node, "lineno", None),
                        )
                    )
                    break

    elif slug == "apply-transform-over-each-element-in-array" and language == "javascript":
        forbidden_map = re.compile(
            r"(?:\.\s*map\s*\(|\[\s*['\"]map['\"]\s*\]\s*\(|Array\s*\.\s*prototype\s*\.\s*map\b)"
        )
        match = forbidden_map.search(source)
        if match is not None:
            issues.append(
                _issue(
                    slug,
                    "restriction_violation_array_map",
                    "2635 转换数组中的每个元素不得使用 Array.prototype.map",
                    source.count("\n", 0, match.start()) + 1,
                )
            )

    return issues
