# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

从所有边界陆地 DFS 清零，剩余陆地均为飞地。

## 复杂度

时间 `O(mn)`，栈最坏 `O(mn)`。

## 边界条件与本地验证

- 已完成 `py_compile` 和边界连通断言。
