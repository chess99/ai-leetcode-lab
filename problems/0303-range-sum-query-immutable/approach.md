# 解题记录

- Profile：terra-medium

## 思路

初始化时构建前缀和数组，prefix[i] 表示前 i 个元素之和。查询 [left, right] 为 prefix[right+1] - prefix[left]。

## 复杂度

初始化 O(n)，单次查询 O(1)，额外空间 O(n)。

## 边界条件与本地验证

left=0 时减去 prefix[0]；单元素区间和包含该元素；数组可包含负数。
