# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

从两个数组的有效末尾开始写入 `nums1`。比较 `nums1[m - 1]` 和 `nums2[n - 1]`，把较大者放到末尾空位；这不会覆盖 `nums1` 尚未比较的元素。若 `nums2` 仍有元素，继续复制。

## 复杂度

时间 O(m + n)，额外空间 O(1)。

## 边界条件与本地验证

覆盖空数组、所有 `nums2` 元素更小或更大、重复值及负数。
