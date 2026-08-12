# 解题记录

- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium；轮次：1

## 思路

记 `solve(x)` 为从 0 到 x 的最小费用。最后一次公交跳跃长度为 `j` 时，跳跃前的位置只需考虑 `floor(x/j)` 与 `ceil(x/j)`：前者跳后向前走余数，后者跳后倒退多出的距离。再与全程步行比较并记忆化。每次递归的位置至少按跳跃倍数缩小。

## 复杂度

状态数为 `O(k log target)`，每个状态枚举 k 种公交，时间 `O(k² log target)`，空间 `O(k log target)`；k 不超过 10。

## 边界条件与本地验证

处理 target 为 0/1、整除和向上凑整不缩小的情况。两个官方样例分别得到 33、26；另与小坐标有界 Dijkstra 随机对拍 3000 组通过。
