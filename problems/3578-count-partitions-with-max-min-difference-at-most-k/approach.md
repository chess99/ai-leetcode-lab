# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

双单调队列维护每个右端点可行窗口的最小左端点，dp[i] 是前 i 个元素的方案数，利用前缀和快速累加所有合法前驱。

## 复杂度

时间 O(n)，空间 O(n)。

## 边界条件与本地验证

待填写。
