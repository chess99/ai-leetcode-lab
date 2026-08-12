# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

两个子序列可重叠，因此目标等价于任选元素的 XOR。维护线性基并贪心生成最大 XOR。

## 复杂度

时间 `O(31n)`，空间 `O(31)`。

## 边界条件与本地验证

处理零元素和线性相关元素。
