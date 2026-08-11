# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

按起点排序，每轮从可接上的片段选最远终点；不能扩展即无解。

## 复杂度

时间 `O(n log n)`，空间取决于排序。

## 边界条件与本地验证

- 已完成 `py_compile` 和可拼接/不可拼接断言。
