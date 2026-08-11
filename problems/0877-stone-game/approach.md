# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

偶数堆且总数为奇数时，先手可预先选择奇/偶下标之一并始终取该类，必能获得较大和，故恒胜。

## 复杂度

时间和空间 `O(1)`。

## 边界条件与本地验证

- 已完成 `py_compile` 和题目约束内断言。
