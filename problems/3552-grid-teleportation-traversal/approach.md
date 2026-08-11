# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

用 0-1 BFS：相邻移动权重为 1，同字母传送权重为 0；每种字母只展开一次。

## 复杂度

时间 O(mn)，空间 O(mn)。不可达时返回 -1。

## 边界条件与本地验证

待填写。
