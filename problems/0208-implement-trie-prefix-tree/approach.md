# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1（本地预解，未发起远程测试或提交）

## 思路

Trie 节点保存子节点映射和单词结束标记。插入逐字符建节点；查询走完整路径并检查结束标记；前缀查询只要求路径存在。

## 复杂度

单次操作时间 `O(L)`，空间为所有已插入字符数。

## 边界条件与本地验证

- 前缀存在不代表完整单词存在。
- 多单词可共享前缀。

本地执行 `insert/search/startsWith` 官方操作序列并通过 `py_compile`。
