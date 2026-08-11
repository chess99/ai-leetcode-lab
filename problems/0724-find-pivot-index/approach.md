# 解题记录

- Profile：terra-medium

## 思路

维护左侧和及总和，当前位置满足 left == total-left-current 时返回。

## 复杂度

时间 O(n)，空间 O(1)。

## 边界条件与本地验证

首尾位置均允许成为中心索引。
