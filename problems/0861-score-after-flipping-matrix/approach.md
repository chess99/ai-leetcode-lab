# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

先保证每行最高位为 1；其余列独立取翻转前后较多的 1，按位权累加。

## 复杂度

时间 O(mn)，空间 O(1)。

## 边界条件与本地验证

本地对示例和单行断言并执行 py_compile。
