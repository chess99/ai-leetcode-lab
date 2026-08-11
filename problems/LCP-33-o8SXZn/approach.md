# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

枚举全体蓄水次数。每个水缸的所需桶容量为向上取整 `vat / 次数`，不足部分升级；总操作数取最小。

## 复杂度

时间复杂度 O(max(vat) × n)，额外空间复杂度 O(1)。

## 边界条件与本地验证

所有需求为 0 时不需要操作。已进行 Python 语法检查及最小断言。
