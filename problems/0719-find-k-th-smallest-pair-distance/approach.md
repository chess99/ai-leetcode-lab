# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

排序后在距离值域二分。双指针统计距离不大于 mid 的数对数，若数量至少 k 则缩小上界。

## 复杂度

排序 O(n log n)，二分统计 O(n log R)，空间 O(1)（不计排序）。

## 边界条件与本地验证

重复数产生距离零；双指针单调移动不会漏计。
