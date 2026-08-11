# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

枚举右端点，维护所有至多为 `right-indexDifference` 的下标中最小值和最大值及其位置。当前值只需与这两个极值比较，就能判断是否存在足够大的数值差。

## 复杂度

时间 `O(n)`，空间 `O(1)`。

## 边界条件与本地验证

`indexDifference=0` 时允许同一位置；`valueDifference=0` 会立即匹配。
