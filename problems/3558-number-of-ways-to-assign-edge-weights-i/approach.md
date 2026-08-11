# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

先 BFS 求根到最深节点的边数 d。路径上权重为 1 的边数必须为奇数，二进制选择中恰有一半满足。

## 复杂度

时间 O(n)，空间 O(n)，答案为 2^(d-1)。

## 边界条件与本地验证

待填写。
