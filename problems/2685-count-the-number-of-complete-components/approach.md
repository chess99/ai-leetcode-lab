# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
DFS 获取每个连通分量的节点数和度数和。完全图的度数和正好为 `size*(size-1)`。
## 复杂度
时间 `O(n+e)`，空间 `O(n+e)`。
## 边界条件与本地验证
孤立节点是完整分量；边计入两次故比较度数和。已验证题面样例。
