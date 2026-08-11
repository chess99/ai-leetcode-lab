# 解题记录

- Profile：terra-medium

## 思路

筛选 referee_id 不为 2 或为 NULL 的客户；NULL 不能用普通不等号直接覆盖。

## 复杂度

时间 O(n)，空间 O(1)。

## 边界条件与本地验证

无推荐人的 NULL 行保留，推荐人为 2 的行排除。
