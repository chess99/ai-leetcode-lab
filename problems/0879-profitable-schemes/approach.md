# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

0/1 背包状态 `dp[used][profit]`，利润维度封顶 minProfit 表示已达标。逐项目时人数和利润倒序更新，保证每项目只选一次。最终汇总所有人数不超过 n 且利润达标的方案。

## 复杂度

项目数 M，时间 `O(M·n·minProfit)`，空间 `O(n·minProfit)`。

## 边界条件与本地验证

minProfit=0 时空方案也计入；利润封顶防止状态扩张；人数不足自然跳过。本地 n/M 小规模枚举所有项目子集对拍。
