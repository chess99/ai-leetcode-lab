# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

先计算解码长度但不展开；倒序把 k 映射回重复前的下标，遇到字母时即得到答案。

## 复杂度

时间 `O(n)`，空间 `O(1)`。

## 边界条件与本地验证

- 已完成 `py_compile` 和重复边界断言。
