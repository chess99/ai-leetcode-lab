# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

将 nums 放入集合，扫描链表；当前节点在集合中且下一个节点不在时，刚好结束一个连通分量。

## 复杂度

时间和空间均为 `O(n)`。

## 边界条件与本地验证

- 单节点与相邻分量均覆盖；已完成 `py_compile` 和断言。
