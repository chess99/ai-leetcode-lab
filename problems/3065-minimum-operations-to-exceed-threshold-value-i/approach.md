# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

最终数组中所有元素都必须不小于 k，因此每个小于 k 的元素都恰好需要被移除一次。

## 复杂度

时间复杂度 O(n)，额外空间复杂度 O(1)。

## 边界条件与本地验证

等于 k 的元素无需操作。已进行 Python 语法检查及样例断言。
