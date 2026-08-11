# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

先以员工 id 建索引，再从给定员工用栈遍历所有直属及间接下属，累加重要度。

## 复杂度

时间和索引空间均为 `O(n)`。

## 边界条件与本地验证

- 没有下属时只返回本人重要度。
- 本地执行 `py_compile` 并断言多层组织结构。
