# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

排列中全局逆序均为局部逆序当且仅当每个值与其下标差不超过一；否则存在跨越至少一个位置的全局逆序。

## 复杂度

时间 `O(n)`，空间 `O(1)`。

## 边界条件与本地验证

- 本地 `py_compile` 和真/假案例断言通过。
