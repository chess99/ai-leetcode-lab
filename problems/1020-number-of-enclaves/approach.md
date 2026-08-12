# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

从所有边界陆地 DFS 清零，剩余陆地均为飞地。

## 复杂度

时间 `O(mn)`，栈最坏 `O(mn)`。

## 边界条件与本地验证

- 单行、单列网格的所有陆地都接触边界。对 3000 个随机网格用独立 BFS 标记边界可达陆地，与原地 DFS 结果对拍。
