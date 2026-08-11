# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

建立穷者指向富者的图，记忆化 DFS 返回每人可达集合中最安静者。

## 复杂度

时间 `O(V+E)`，空间 `O(V+E)`。

## 边界条件与本地验证

- 本地 `py_compile` 和示例断言通过。
