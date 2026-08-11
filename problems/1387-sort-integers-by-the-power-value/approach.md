# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
记忆化计算 Collatz 幂值，按 `(幂值, 数值)` 排序并取第 k 个。
## 复杂度
取决于 Collatz 链长度；缓存避免重复计算。
## 边界条件与本地验证
覆盖幂值相同的数按数值升序打破平局。
