# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

第 k 个符号等于 `k-1` 二进制中一的个数的奇偶性，每个一对应一次翻转。

## 复杂度

时间 `O(log k)`，空间 `O(1)`。

## 边界条件与本地验证

- n 只限定有效 k；本地 `py_compile` 和基础行断言通过。
