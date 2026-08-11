# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

后序递归传递路径和；不满足 limit 的叶子删除，内部节点两子树皆删后也删除。

## 复杂度

时间 `O(n)`，栈 `O(h)`。

## 边界条件与本地验证

- 完成 `py_compile` 和剪枝断言。
