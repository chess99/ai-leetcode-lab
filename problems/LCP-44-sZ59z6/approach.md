# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

使用栈遍历整棵二叉树，并将节点值放入集合，集合大小就是颜色种类数。

## 复杂度

时间复杂度 O(n)，额外空间复杂度 O(n)。

## 边界条件与本地验证

空子节点直接跳过。已进行 Python 语法检查及最小断言。
