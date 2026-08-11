# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

按 email 分组，保留分组内记录数大于一的邮箱，并将输出列别名设为 Email。

## 复杂度

时间复杂度 O(N)，空间复杂度 O(N)（用于分组）。

## 边界条件与本地验证

邮箱列保证非 NULL；只出现一次的邮箱被 HAVING 排除；同一邮箱出现多次也只输出一行。
