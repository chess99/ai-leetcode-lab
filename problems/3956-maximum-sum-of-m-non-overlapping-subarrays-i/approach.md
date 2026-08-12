# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

DP 按可选子数组数量推进，`dp[i]` 是前 `i` 个元素至多选若干段的最佳和。新段末尾为 `i` 时，起点 `j` 在长度范围内，转移为 `prefix[i] + max(dp[j]-prefix[j])`；用单调队列维护这个最大值。

## 复杂度

`O(mn)` 时间，`O(n)` 空间。

## 边界条件与本地验证

允许少于 `m` 段及全负数组；题面样例为 7，并同递归枚举对拍 500 组小随机数据。
