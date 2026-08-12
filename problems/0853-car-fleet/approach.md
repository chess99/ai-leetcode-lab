# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

按位置从近到远扫描，抵达时间不大于前方最慢车队即会合，否则形成新车队。

## 复杂度

排序主导 `O(n log n)`，空间 `O(n)`。

## 边界条件与本地验证

- 相同抵达时间合并；本地 `py_compile` 和示例断言通过。
