# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

找到区间前一个节点及区间后一个节点，把前者连到 `list2` 头，再找到 `list2` 尾并连回后者。

## 正确性

两次重连恰好跳过 `[a,b]` 的所有节点，并保留其余节点原有顺序。

## 复杂度

时间 `O(length(list1)+length(list2))`，额外空间 `O(1)`。

## 边界条件与本地验证

题目保证 `b < list1.length - 1`，因此被替换区间后至少还有一个节点；已用题目样例链表验证连接顺序。
