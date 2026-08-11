# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

枚举分母和更小的分子，仅保留最大公约数为 1 的分数。

## 复杂度

时间 `O(n² log n)`，空间为输出空间。

## 边界条件与本地验证

- `n=1` 返回空列表。
- 本地验证了题目示例。
