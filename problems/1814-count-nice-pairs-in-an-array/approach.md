# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
等式移项为 `num-rev(num)` 相等，用哈希表在线累计相同键对数。
## 正确性
移项为等价变形，每个此前相同键恰构成一个好对。
## 复杂度
时间 `O(n)`，空间 `O(n)`。
## 边界条件与本地验证
- 验证重复键与取模。
