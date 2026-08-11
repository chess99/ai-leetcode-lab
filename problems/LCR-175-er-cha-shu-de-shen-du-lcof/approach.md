# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

递归计算左右子树最大深度，再加上当前节点。

## 复杂度

时间复杂度 O(n)，额外空间复杂度 O(h)。

## 边界条件与本地验证

空树深度为 0。已进行 Python 语法检查及最小断言。
