# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

将 Employee 自连接：员工行的 managerId 对应经理行的 id，筛选员工工资大于经理工资的记录，并把员工姓名别名为 Employee。

## 复杂度

时间复杂度 O(N)，空间复杂度 O(1)（不计数据库连接执行计划）。

## 边界条件与本地验证

没有经理的员工无法匹配，不会输出；工资相等不满足严格大于条件；可以返回多个符合条件的员工。
