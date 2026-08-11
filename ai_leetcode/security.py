from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

from .config import ROOT


SECRET_PATTERNS = [
    ("LeetCode session", re.compile(r"LEETCODE_SESSION\s*[=:]\s*[^\s'\"]{20,}", re.IGNORECASE)),
    ("LeetCode CSRF token", re.compile(r"(?:LEETCODE_CSRF_TOKEN|csrftoken)\s*[=:]\s*[A-Za-z0-9_-]{16,}", re.IGNORECASE)),
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("generic API key", re.compile(r"(?:api[_-]?key|secret[_-]?key)\s*[=:]\s*[^\s'\"]{20,}", re.IGNORECASE)),
]

FORBIDDEN_PREFIXES = (".secrets/", ".runtime/")
FORBIDDEN_EXACT = {".ai/identity.env"}


def scan_added_lines(lines: Iterable[str]) -> list[str]:
    findings: list[str] = []
    for number, line in enumerate(lines, 1):
        if not line.startswith("+") or line.startswith("+++"):
            continue
        content = line[1:]
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(content):
                findings.append(f"第 {number} 行疑似包含 {label}")
    return findings


def scan_staged(root: Path = ROOT) -> list[str]:
    names_raw = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "-z"],
        cwd=root,
        check=True,
        capture_output=True,
    ).stdout
    names = [item.decode("utf-8", errors="replace").replace("\\", "/") for item in names_raw.split(b"\0") if item]
    findings = [
        f"禁止提交本地文件：{name}"
        for name in names
        if name in FORBIDDEN_EXACT or any(name.startswith(prefix) for prefix in FORBIDDEN_PREFIXES)
    ]
    diff = subprocess.run(
        ["git", "diff", "--cached", "--no-ext-diff", "--unified=0", "--no-color"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    ).stdout
    findings.extend(scan_added_lines(diff.splitlines()))
    return findings


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8", errors="replace")
    findings = scan_staged()
    if findings:
        print("提交已阻止：暂存内容可能泄露密钥。", file=sys.stderr)
        for finding in findings:
            print(f"- {finding}", file=sys.stderr)
        return 1
    print("密钥扫描通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
