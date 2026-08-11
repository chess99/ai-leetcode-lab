# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

移除 X 后 L/R 顺序必须相同；对应 L 只能左移，R 只能右移，比较它们在两串中的下标即可。

## 复杂度

时间和空间均为 `O(n)`。

## 边界条件与本地验证

- 本地 `py_compile` 和可变换/方向错误断言通过。
