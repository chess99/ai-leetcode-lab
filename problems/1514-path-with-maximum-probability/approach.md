# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

最大堆版 Dijkstra，状态按到达概率从大到小弹出，松弛时相乘更新邻居概率。

## 复杂度

时间 `O((n+e) log n)`，空间 `O(n+e)`。

## 边界条件与本地验证

- 不可达时返回 0。
- 本地验证了题目示例。
