# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

Manacher 求每个位置结束的最长奇回文，并从右侧传播可用长度；翻转字符串同理得到右侧值，枚举分界。

## 复杂度

时间 O(n)，空间 O(n)。

## 边界条件与本地验证

只统计题意要求的奇回文；短串枚举两个不重叠回文核对。
