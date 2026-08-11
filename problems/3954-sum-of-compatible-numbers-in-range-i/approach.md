# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

直接枚举区间 [n-k, n+k] 内的正整数，按位与为 0 时将该数加入总和。

## 复杂度

时间复杂度 O(k)，额外空间复杂度 O(1)。

## 边界条件与本地验证

枚举下界取 1，排除非正整数。已进行 Python 语法检查及最小断言。
