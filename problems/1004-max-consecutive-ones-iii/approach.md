# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

滑动窗口保留至多 k 个零，超过时移动左端，最终窗口即最大长度。

## 复杂度

时间 `O(n)`，空间 `O(1)`。

## 边界条件与本地验证

- 已完成 `py_compile` 和 k=0/示例断言。
