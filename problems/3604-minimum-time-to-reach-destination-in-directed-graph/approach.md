# 解题记录

- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium；Created：2026-08-11T22:15:56Z

## 思路

用 Dijkstra 求最早到达时间。到节点时间为 `t` 时，一条边最早可在 `max(t,start)` 出发，若不晚于 `end` 则在下一单位时间抵达；边等待不会破坏最早到达的最优子结构。

## 复杂度

时间 `O((n+m)log n)`，空间 `O(n+m)`。

## 边界条件与本地验证

无可用出边返回 `-1`，可在节点等待。已覆盖三个样例。
