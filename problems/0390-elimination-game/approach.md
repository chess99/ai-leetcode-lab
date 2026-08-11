# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
维护首项、步长、方向和剩余数量；每轮删除一半，方向或奇数数量决定首项是否前移。
## 复杂度
时间 `O(log n)`，空间 `O(1)`。
## 边界条件与本地验证
`n=1` 返回 1。已断言示例并通过 `py_compile`。
