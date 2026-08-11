# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

枚举第一位小朋友所得糖果。剩余糖果分给后两人时，第二人的可取范围为 `max(0,remaining-limit)` 到 `min(limit,remaining)`，区间长度即方案数。

## 复杂度

时间 `O(limit)`，空间 `O(1)`。

## 边界条件与本地验证

第一人下界保证其余两人最多能容纳剩余糖果；无效区间贡献零。
