# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

矩形两条对角线有相同中点和长度。按该键分组任意两条对角线，取一端到另一对角线两端的距离乘积为面积。

## 复杂度

时间最坏 `O(n^4)`，空间 `O(n^2)`。

## 边界条件与本地验证

- 无矩形返回零；完成 `py_compile` 和矩形断言。
