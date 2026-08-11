# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

前序首值为根，前序下一值定位左子树根；借助后序下标表确定左子树大小并递归切分。

## 复杂度

时间 O(n)，空间 O(n)。

## 边界条件与本地验证

单节点直接返回；本地重遍历断言并执行 py_compile。
