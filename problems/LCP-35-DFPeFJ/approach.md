# 解题记录

- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium；轮次：1

## 思路

把 `(城市,剩余电量)` 作为最短路状态。可以在当前城市花 charge[city] 时间充一单位电，或在电量足够时沿道路行驶，耗时和耗电都等于道路距离。所有边权非负，用 Dijkstra；首次弹出终点城市即为最优。

## 复杂度

状态 `O(N*cnt)`，时间 `O((N*cnt+M*cnt) log(N*cnt))`，空间 `O(N*cnt+M)`。

## 边界条件与本地验证

覆盖起点等于终点、道路耗电超过容量和不同城市充电价。两个官方样例得到 43、38。
