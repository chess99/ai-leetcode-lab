# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

递归携带上界，当前前序值未超过上界才创建节点；左树上界为节点值，右树沿用父上界。

## 复杂度

时间 `O(n)`，递归空间 `O(h)`。

## 边界条件与本地验证

- 已完成 `py_compile` 和典型 BST 结构断言。
