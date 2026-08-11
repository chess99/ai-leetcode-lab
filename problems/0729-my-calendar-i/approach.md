# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

保存已预订的半开区间。新区间与任一区间满足 `start < oldEnd and oldStart < end` 即重叠并拒绝，否则加入。

## 复杂度

每次预订扫描已有记录，时间 `O(n)`，存储 `O(n)`。

## 边界条件与本地验证

- 端点相接不重叠。
- 本地执行 `py_compile` 和题目操作序列断言。
