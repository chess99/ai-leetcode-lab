# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

0-1 背包中 `dp[sum]` 记录达到该和的最大元素数。每个数倒序更新，保证最多使用一次；不可达状态设为极小值。

## 复杂度

时间 `O(n*target)`，空间 `O(target)`。

## 边界条件与本地验证

无法达到目标返回 -1；倒序防止重复选择同一元素。
