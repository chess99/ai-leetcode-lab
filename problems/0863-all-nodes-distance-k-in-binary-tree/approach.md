# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

建立父指针后从 target 做无向图 BFS，收集距离恰为 k 的节点。

## 复杂度

时间 O(n)，空间 O(n)。

## 边界条件与本地验证

访问集防止父子回走；k=0 返回目标。本地构造树断言并执行 py_compile。
