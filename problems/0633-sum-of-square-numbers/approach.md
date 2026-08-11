# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

设两个非负数指针 left=0、right=floor(sqrt(c))。由于平方和随 left 增大而增大、随 right 减小而减小：当前平方和小于 c 时右侧已不足，增加 left；大于 c 时减少 right；相等则找到一组解。两指针相遇仍未相等则不存在解。

## 复杂度

- 指针最多各移动 O(sqrt(c)) 次，时间 O(sqrt(c))。
- 额外空间 O(1)。

## 边界条件与本地验证

- c=0 时 0²+0²=0，应返回真。
- 完全平方数可由 0²+b² 表示。
- isqrt 直接给出精确整数平方根，避免浮点边界误差。

本地对题目两个示例、零、完全平方数和 2^31-1 做最小断言，并执行 py_compile 语法检查。
