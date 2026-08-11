# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

将表自连接：左表为待分类节点，右表寻找以左表 `id` 为 `p_id` 的子节点。`p_id IS NULL` 的节点优先判为 Root；其余节点若聚合后的子节点数量为 0 则为 Leaf，否则为 Inner。

## 复杂度

设节点数为 `n`。自连接和分组的实际开销依赖索引与执行计划；在 `p_id` 上有索引时通常接近 `O(n)`，结果空间为 `O(n)`。

## 边界条件与本地验证

- 单节点树虽没有子节点，仍应优先标为 Root。
- 自连接可能为一个父节点得到多行，使用 `COUNT(child.id)` 和分组消除重复。
- 以题目示例静态核对得到 Root、Inner 和 Leaf 三种分类；SQL 聚合列均已纳入 `GROUP BY` 或聚合函数，兼容 MySQL 的严格分组模式。
