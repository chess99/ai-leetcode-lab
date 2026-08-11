# 解题记录

- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium；Created：2026-08-11T22:15:56Z

## 思路

筛出数组下标范围内的质数，将质数下标元素累计到 A，其余元素进入 B，返回两者和的绝对差。

## 复杂度

时间 `O(n log log n)`，空间 `O(n)`。

## 边界条件与本地验证

0 和 1 不是质数下标；已覆盖两个样例。
