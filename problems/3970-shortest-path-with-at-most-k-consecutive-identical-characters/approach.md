# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

路径合法性不仅取决于当前节点，还取决于末尾连续相同标签的长度。把状态扩展为 `(node, run)`：若下一节点标签相同则 `run+1`，否则重置为 1；超过 `k` 的转移丢弃。所有边权为正，在扩展状态图上运行 Dijkstra。

## 复杂度

状态数 `O(nk)`、边转移数 `O(mk)`，时间 `O((n+m)k log(nk))`，空间 `O(nk+m)`。

## 边界条件与本地验证

`n=1` 时初始标签段长度为 1、距离为 0；验证三组样例，并与小图状态 Bellman-Ford 对拍。
