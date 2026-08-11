# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

排序后定义 `count_at_most(x)` 为和不超过 `x` 的数对数量。双指针中，若最左与最右之和不超过 `x`，则该左端点与中间所有位置均可配对，累计后左指针右移；否则右指针左移。所求区间数量等于 `count_at_most(upper) - count_at_most(lower - 1)`。

## 复杂度

排序耗时 `O(n log n)`，两次双指针为 `O(n)`；除排序外额外空间 `O(1)`。

## 边界条件与本地验证

数组可含负数和重复值；使用 `lower - 1` 将闭区间下界自然纳入；长度不足两个时结果为 `0`。
