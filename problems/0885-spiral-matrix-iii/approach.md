# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

按右、下、左、上螺旋行走，水平段结束后步长加一，仅收集矩阵内坐标。

## 复杂度

时间与行走范围成正比，输出空间 `O(rows*cols)`。

## 边界条件与本地验证

- 已完成 `py_compile` 和单行/示例断言。
