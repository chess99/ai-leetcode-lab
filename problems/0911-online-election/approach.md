# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

预处理每次投票后的领先者，平票时最新得票者领先；查询时二分最后一个不超过 t 的时间。

## 复杂度

初始化 `O(n)`，查询 `O(log n)`，空间 `O(n)`。

## 边界条件与本地验证

- 平票以新候选人覆盖；已完成 `py_compile` 和查询断言。
