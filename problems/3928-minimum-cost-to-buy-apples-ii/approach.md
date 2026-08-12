# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

将每条路换算为往返成本 `cost * (tax + 1)`。以所有城市的本地苹果价作为初始距离进行多源 Dijkstra，所得即每城最低买入成本。

## 复杂度

`O((n+m) log n)` 时间，`O(n+m)` 空间。

## 边界条件与本地验证

三个题面样例均通过，结果分别为 `[6,3]`、`[8,4,6]`、`[5,11,1]`。
