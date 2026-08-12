# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

按树高排序，依次从当前位置 BFS 到下一棵树；任一步不可达立即返回负一，累计最短距离。

## 复杂度

每次 BFS O(mn)，总时间 O(Tmn)，空间 O(mn)。

## 边界条件与本地验证

障碍值为零不可进入；没有树时距离为零。
