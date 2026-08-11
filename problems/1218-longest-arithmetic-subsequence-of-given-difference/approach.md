# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

`dp[v]` 保存以值 `v` 结尾的最长长度；当前值从 `v-difference` 的状态延长。

## 复杂度

时间 `O(N)`，空间 `O(N)`。

## 边界条件与本地验证

- 覆盖题面三个示例和差值为零。
