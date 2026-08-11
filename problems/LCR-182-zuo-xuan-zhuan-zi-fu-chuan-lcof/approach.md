# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

左旋转 k 位等价于拼接从 k 开始的后缀和前 k 位前缀。

## 复杂度

时间复杂度 O(n)，额外空间复杂度 O(n)。

## 边界条件与本地验证

k 为 0 时结果保持原串。已进行 Python 语法检查及最小断言。
