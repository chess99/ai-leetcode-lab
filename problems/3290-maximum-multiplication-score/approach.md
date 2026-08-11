# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

扫描 `b` 并倒序更新四阶段动态规划，保证每个元素至多被选一次。

## 复杂度

时间 `O(len(b))`，空间 `O(1)`。

## 边界条件与本地验证

覆盖负数乘积和恰好选择四个元素。
