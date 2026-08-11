# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

后序递归剪枝，先处理左右子树；节点值为零且剪枝后无子树时删除，否则保留。

## 复杂度

时间 `O(n)`，递归栈 `O(h)`。

## 边界条件与本地验证

- 全零树返回空；已完成 `py_compile` 和断言。
