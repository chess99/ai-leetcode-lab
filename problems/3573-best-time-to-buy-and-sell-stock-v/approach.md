# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

动态规划维护完成 t 笔交易后的空仓、持多仓和持空仓最大收益。每天只从前一天状态转移，保证平仓后不能同日再开仓。

## 复杂度

时间 O(nk)，空间 O(k)。

## 边界条件与本地验证

待填写。
