# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

按 `nums2` 降序遍历，当前值作为所选元素的最小 `nums2`。用最小堆保留已遍历元素中最大的 `k` 个 `nums1`，堆大小达到 `k` 时计算分数并更新答案。

## 复杂度

排序和堆操作均为 `O(n log n)`，空间 `O(n)`。

## 边界条件与本地验证

`k=1` 时每个元素独立比较；`nums1` 可为 0。已验证两个题面样例。
