# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

分三次原地遍历。先在每个原节点后插入其副本，使原节点的 random 若存在时，副本随机指针就是 `original.random.next`；第二遍设置所有副本 random；第三遍拆开交织链表，恢复原 next 并串起副本链。无需哈希表，且原节点与其副本的相邻关系让随机映射可 O(1) 找到。

## 复杂度

三遍各线性扫描，时间 O(n)，除输出链表外额外空间 O(1)。

## 边界条件与本地验证

本地检查空链、random 为 null、自指向、前后指向和原链在复制后仍保持原有 next/random 关系。
