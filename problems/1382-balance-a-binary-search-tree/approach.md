# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
中序遍历取得有序节点列表，再递归选择中点作为根重建平衡 BST。
## 复杂度
时间 `O(N)`，空间 `O(N)`。
## 边界条件与本地验证
覆盖退化单链与单节点树。
