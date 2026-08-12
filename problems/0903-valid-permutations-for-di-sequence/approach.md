# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

dp 表示当前长度下按相对排名结尾的方案数；I 用前缀和、D 用后缀和完成转移。

## 复杂度

时间 O(n²)，空间 O(n)。

## 边界条件与本地验证

每轮长度加一，结果为所有末排名状态之和并取模。
