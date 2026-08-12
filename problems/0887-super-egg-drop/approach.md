# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

dp[e] 表示给定尝试次数能确定的最大楼层数，新增一次尝试后为破碎与不碎两种子问题之和再加当前层。

## 复杂度

时间 O(k·moves)，空间 O(k)。

## 边界条件与本地验证

倒序更新避免复用本轮状态；首次覆盖 n 楼时的 moves 即最优。
