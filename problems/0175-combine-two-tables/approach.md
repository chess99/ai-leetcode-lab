# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

以 Person 为主表，按 personId 左连接 Address。这样每个人都会保留；没有匹配地址时 city 和 state 自然为 NULL。

## 复杂度

时间复杂度 O(P + A)，空间复杂度 O(1)（不计查询结果与数据库执行计划）。

## 边界条件与本地验证

验证了 Person 无地址时仍返回该行且地址列为 NULL；Address 中没有对应 Person 的行不会出现在结果中。
