# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

把状态扩展为 `(节点, 剩余电量)`。离开节点统一扣除 `cost[u]`，边权仍为时间；在扩展图上跑 Dijkstra。堆键使用 `(时间, -剩余电量)`，因此第一次弹出目标节点时同时满足时间最小、同时间剩余电量最大。

## 复杂度

状态数 `O(n·power)`，时间 `O((n·power+E·power)log(n·power))`，空间 `O(n·power)`。

## 边界条件与本地验证

起终点相同直接由初始状态返回；电量不足以离开时不扩展。本地验证三个样例，并对小图用扩展状态 Bellman-Ford 对拍。
