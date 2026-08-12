# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

倒序把水格恢复为陆地并查集，连接相邻陆地及虚拟顶底节点；首次顶底连通即答案。

## 复杂度

时间 O(row·col·α)，空间 O(row·col)。

## 边界条件与本地验证

四方向连接；小网格逐日 BFS 判定过河核对。
