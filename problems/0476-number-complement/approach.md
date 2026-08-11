# 解题记录

- Profile：terra-medium

## 思路

用 bit_length 构造与 num 有效位等长的全一掩码，再与 num 异或翻转有效位。

## 复杂度

时间 O(1)，空间 O(1)。

## 边界条件与本地验证

掩码不包含前导零；num=1 的补数为零。
