# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

每只猪在测试时间内有“第几轮死亡”及“始终存活”共 `minutesToTest/minutesToDie+1` 种状态。p 只猪能区分 `states^p` 个桶，求最小 p 使其覆盖桶数即可。

## 复杂度

循环次数即答案，时间 `O(log_states buckets)`，空间 `O(1)`。

## 边界条件与本地验证

一个桶无需猪；测试轮数至少一轮。验证题面样例和状态幂边界前后桶数。
