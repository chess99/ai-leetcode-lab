# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
裴蜀定理：可量出目标当且仅当不超过总容量，且为两容量最大公约数的倍数。
## 复杂度
时间 `O(log(min(x,y)))`，空间 `O(1)`。
## 边界条件与本地验证
目标为 0 可行；容量为 0 由 `gcd` 处理。本地断言示例并通过 `py_compile`。
