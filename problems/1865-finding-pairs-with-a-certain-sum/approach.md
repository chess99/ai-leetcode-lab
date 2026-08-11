# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

保存 nums2 的频次表。更新时维护旧值和新值频次；查询枚举 nums1，查找补数频次。

## 正确性

频次表始终等于当前 nums2 分布，每个 nums1 元素可配对数量正是其补数频次，求和不重不漏。

## 复杂度

更新 `O(1)`，查询 `O(len(nums1))`，空间 `O(len(nums2))`。

## 边界条件与本地验证

重复数字按频次计数；已用样例验证。
