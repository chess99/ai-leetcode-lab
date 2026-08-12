# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路
- 语言：MySQL

按客户分组，购买的不同产品数等于 Product 总数时即购买全部产品。

## 复杂度

实际由数据库执行计划决定；一次分组和子查询。

## 边界条件与本地验证

- 使用 DISTINCT 防重复；完成 MySQL 静态检查。
