# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

反向图拓扑剥离：终端节点安全，删除它们的入边后新出度零节点也安全；最终剩余节点在或可达环。

## 复杂度

时间和空间均为 `O(V+E)`。

## 边界条件与本地验证

- 环节点不会被剥离；已完成 `py_compile` 和示例断言。
