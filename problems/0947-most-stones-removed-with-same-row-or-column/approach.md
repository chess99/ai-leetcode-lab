# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

并查集连接行节点与取反后的列节点；每个连通分量留一块石头，答案为石头数减分量数。

## 复杂度

时间近似 `O(n)`，空间 `O(n)`。

## 边界条件与本地验证

- 行列编号隔离，单石头为零；已完成 `py_compile` 和断言。
