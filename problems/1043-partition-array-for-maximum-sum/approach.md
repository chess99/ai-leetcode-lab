# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

`dp[i]` 为前 i 项最优值，枚举末段长度不超过 k 并维护该段最大值转移。

## 复杂度

时间 `O(nk)`，空间 `O(n)`。

## 边界条件与本地验证

- 完成 `py_compile` 和示例断言。
