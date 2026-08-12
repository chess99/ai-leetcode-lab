# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
先取 `1` 到 `target // 2` 中尽可能多的数，再从 `target` 起连续取剩余数，使用等差数列求和。若 `target` 为偶数，`target / 2` 可以选一次，因为题目只禁止两个不同下标的元素之和等于 `target`。
## 复杂度
时间和空间均为 `O(1)`。
## 边界条件与本地验证
结果按模数返回；特别验证了 `n = 1, target = 2` 应选择 `[1]`，以及题面样例。
