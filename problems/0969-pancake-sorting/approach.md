# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

从最大未放置值起，至多两次前缀翻转将其移到目标末位。

## 复杂度

时间 `O(n^2)`，翻转序列空间 `O(n)`。

## 边界条件与本地验证

- 完成 `py_compile` 和排序结果断言。
