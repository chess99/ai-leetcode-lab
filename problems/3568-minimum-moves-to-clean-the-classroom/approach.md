# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

对“位置、已收集垃圾掩码、剩余能量”做 BFS。相同位置和掩码仅保留剩余能量最大的状态，R 格将能量重置。

## 复杂度

状态至多 O(mn·2^L·energy)，L≤10；第一次收齐垃圾即为最短步数。

## 边界条件与本地验证

待填写。
