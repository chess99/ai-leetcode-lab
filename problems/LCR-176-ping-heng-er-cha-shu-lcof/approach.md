# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

后序递归返回高度，不平衡时返回 -1 并向上传播。

## 复杂度

时间复杂度 O(n)，额外空间复杂度 O(h)。

## 边界条件与本地验证

空树平衡。已进行 Python 语法检查及最小断言。
