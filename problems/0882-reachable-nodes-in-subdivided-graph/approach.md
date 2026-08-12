# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

对原图做 Dijkstra，距离表示到原节点的步数；每条边两端剩余步数之和最多可访问该边的插入节点数。

## 复杂度

时间 O((n+E)log n)，空间 O(n+E)。

## 边界条件与本地验证

不可达端贡献为零；原节点和细分节点分别统计，避免重复。
