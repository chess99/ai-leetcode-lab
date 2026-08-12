# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

先按左端点排序，将重叠或整数意义上相接（下一左端点不超过当前右端点加一）的区间合并。再对每个合并区间减去闭区间 `[freeStart,freeEnd]`，最多留下左右两段。

## 复杂度

时间 `O(n log n)`，空间 `O(n)`。

## 边界条件与本地验证

减法端点使用 `freeStart-1` 与 `freeEnd+1`；验证完全覆盖、无交集、从中间切成两段和相接区间。
