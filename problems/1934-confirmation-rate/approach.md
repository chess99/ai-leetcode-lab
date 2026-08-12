# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

以 Signups 为主表左连接 Confirmations，MySQL 将布尔表达式转为 0/1，对 confirmed 条件取平均并四舍五入两位。没有确认记录时 `AVG` 为 `NULL`，用 `COALESCE` 转为 0。

## 正确性

左连接保留无确认记录用户，`COALESCE` 将 `AVG` 的空值按题意输出 0；有记录时布尔平均正是确认比例。

## 复杂度

扫描并按用户分组，复杂度由索引和执行计划决定。

## 边界条件与本地验证

无确认记录用户返回 0.00；已按样例逻辑核对。
