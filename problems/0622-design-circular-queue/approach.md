# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

使用固定数组、队首下标和当前大小。入队位置为 `(front + size) % capacity`，出队移动队首；大小可区分空和满，因此不浪费数组槽位。队尾由 `(front + size - 1) % capacity` 得到。

## 复杂度

所有操作时间均为 `O(1)`，数组空间 `O(k)`。

## 边界条件与本地验证

- 空队列的 Front/Rear 为 `-1`。
- 满队列拒绝入队，空队列拒绝出队。
- 出队再入队验证下标回绕。
- 本地执行 `py_compile` 并断言题目操作序列与容量为一的队列。
