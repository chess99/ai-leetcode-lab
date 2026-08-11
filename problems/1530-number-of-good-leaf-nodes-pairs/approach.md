# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
后序 DFS 返回子树叶子到当前节点的距离；左右距离和不超过限制时计数。
## 复杂度
时间 `O(ND²)`，空间 `O(ND)`。
## 边界条件与本地验证
覆盖单叶和跨左右子树配对。
