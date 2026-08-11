# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

使用固定容量数组、头下标 front 和当前元素数量 size。队尾下一个写入位置恒为 (front+size) mod capacity；队尾元素位置为 (front+size-1) mod capacity。前插时先让 front 循环左移，后插时写入队尾位置；删除仅调整 front 或 size。

通过 size 区分空与满，避免仅用首尾指针时两种状态重合。

## 复杂度

- 所有插入、删除、查询和状态判断都只做常数次数组访问，时间 O(1)。
- 固定数组占用 O(k) 空间，k 为容量。

## 边界条件与本地验证

- 队空时查询返回 -1，删除返回 False。
- 队满时插入返回 False，已有元素不被覆盖。
- 头下标在两端插入删除时通过取模正确回绕。

本地执行题目示例操作序列，并额外验证容量 1、空队删除和跨数组边界回绕，随后执行 py_compile 语法检查。
