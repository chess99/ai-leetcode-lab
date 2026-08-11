# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

设左段和为 `left`、全数组和为 `total`，差值为 `left - (total - left) = 2 * left - total`。其中 `2 * left` 恒为偶数，因此差值的奇偶性完全由 `total` 决定：总和为偶数时全部 `n - 1` 个分区都有效，否则一个也没有。

## 复杂度

设数组长度为 `n`。求和时间复杂度为 `O(n)`，额外空间复杂度为 `O(1)`。

## 边界条件与本地验证

分区两侧必须非空，候选分割点恰有 `n - 1` 个。总和为奇数时，无论分割位置如何都不满足。
