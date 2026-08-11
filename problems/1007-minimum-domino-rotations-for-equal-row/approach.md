# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

候选值只能是首张骨牌两面之一；分别统计把两行变成候选值的旋转数。

## 复杂度

时间 `O(n)`，空间 `O(1)`。

## 边界条件与本地验证

- 无可行候选返回 -1；已完成 `py_compile` 和断言。
