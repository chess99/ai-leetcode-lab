# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

使用方法链依次筛选体重大于 100 的动物、按体重降序排序，并只保留名称列。

## 复杂度

时间复杂度 O(n log n)，额外空间复杂度 O(n)。

## 边界条件与本地验证

体重恰好为 100 的动物不计入。已进行本地 Pandas 断言。
