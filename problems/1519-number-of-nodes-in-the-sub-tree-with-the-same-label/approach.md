# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

树形 DFS 返回子树的 26 个标签计数，合并孩子计数后记录当前标签数量。

## 复杂度

时间 `O(26n)`，空间 `O(n)`。

## 边界条件与本地验证

- 单节点子树计数为 1。
- 本地验证了题目示例。
