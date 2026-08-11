# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

遍历 grid2 的每个岛屿并用 DFS/BFS 淹没它，同时检查所有格子在 grid1 中是否为陆地。

## 正确性

搜索恰访问一个完整 grid2 岛；它为子岛当且仅当搜索到的每格都被 grid1 覆盖。

## 复杂度

时间 `O(mn)`，搜索栈空间最坏 `O(mn)`。

## 边界条件与本地验证

任一未覆盖格会使整岛无效；已用样例验证。
