# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

对每个连通分量 BFS 二染色，边两端颜色相同即不能二分。

## 复杂度

时间和空间均为 `O(V+E)`。

## 边界条件与本地验证

- 覆盖非连通图和奇环；已完成 `py_compile` 和断言。
