# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

dp 按播放长度和已用歌曲数转移，可选择新歌或不在冷却区的旧歌。

## 复杂度

时间 O(goal·n)，空间 O(goal·n)。

## 边界条件与本地验证

旧歌数量为 max(0, used-k)，结果取模。
