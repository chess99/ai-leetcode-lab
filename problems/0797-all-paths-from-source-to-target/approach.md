# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

在 DAG 中从零号节点深度优先枚举，每抵达终点即记录当前路径。

## 复杂度

与输出路径总长度成正比，递归空间为最大路径长。

## 边界条件与本地验证

- 已完成 `py_compile` 和多路径/单节点断言。
