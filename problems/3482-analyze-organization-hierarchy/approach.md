# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

第一个递归 CTE 从 CEO 向下计算每名员工层级；第二个递归 CTE 为每名员工生成自己及全部直接、间接下属的闭包。连接工资表后按经理聚合，行数减一得到团队大小，工资求和得到预算，最后按题意排序。

## 复杂度

设层级闭包含 R 行，时间和中间空间主要为 O(R)。

## 边界条件与本地验证

叶节点闭包仍包含自己，因此 team_size 为0、budget为本人薪资。使用 MySQL 8 WITH RECURSIVE。
