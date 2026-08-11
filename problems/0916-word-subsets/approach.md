# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

取 words2 所有字符需求的逐字符最大频次，再筛选能覆盖该需求的 words1。

## 复杂度

时间与总字符数成正比，额外空间为字母表大小。

## 边界条件与本地验证

- 已完成 `py_compile` 和合并频次断言。
