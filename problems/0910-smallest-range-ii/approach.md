# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

排序后枚举分界，左侧加 k、右侧减 k；由两侧端点计算新范围并取最小。

## 复杂度

时间 `O(n log n)`，空间取决于排序。

## 边界条件与本地验证

- 已完成 `py_compile` 和单值/示例断言。
