# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

状态压缩 dp[mask][last] 保存覆盖 mask 并以 last 结束的最短串，转移时拼接下一个词的非重叠后缀。

## 复杂度

时间 O(2^n·n²·L)，空间 O(2^n·n·L)。

## 边界条件与本地验证

枚举最大后后缀重叠；最终从覆盖全体词的末词状态选最短。
