# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

遇到原子对 `()` 的右括号时，按当前嵌套深度贡献 `2^depth`，所有原子贡献求和。

## 复杂度

时间 `O(n)`，空间 `O(1)`。

## 边界条件与本地验证

- 本地 `py_compile` 和嵌套/并列断言通过。
