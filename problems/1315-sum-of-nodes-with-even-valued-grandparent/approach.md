# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
DFS 栈携带父与祖父节点，当前节点的祖父为偶数时累加值。
## 复杂度
时间 `O(N)`，空间 `O(N)`。
## 边界条件与本地验证
覆盖叶子及不足两层的树。
