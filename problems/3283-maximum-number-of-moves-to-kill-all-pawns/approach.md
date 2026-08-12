# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

先从每个兵和骑士初始位置在 50×50 棋盘跑 BFS，得到任意关键点间的骑士最短距离。之后用 `game(mask,current)` 做极小极大状态压缩：已吃兵数为偶数时 Alice 取最大，奇数时 Bob 取最小。

## 复杂度

BFS 为 `O(p*2500)`，博弈 DP 为 `O(p^2 2^p)`，空间 `O(p2^p)`，`p<=15`。

## 边界条件与本地验证

双方每步都必须吃一个尚存的兵，最后状态返回 0。3 组样例及小规模独立 BFS+极小极大 oracle 通过，15 个兵约 0.79 秒。
