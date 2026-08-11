# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

维护双向字符映射，逐位验证一一对应关系。

## 复杂度

时间 O(总字符数)，空间 O(字符集)。

## 边界条件与本地验证

双向表排除多对一；本地对示例断言并执行 py_compile。
