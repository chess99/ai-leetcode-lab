# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

SQL 使用 LIKE 和 REGEXP 分别计算四个模式标志，并按样本编号排序。

## 复杂度

单次扫描结果集。

## 边界条件与本地验证

静态核查了列名、布尔表达式及排序要求。
