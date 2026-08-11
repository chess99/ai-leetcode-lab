# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

维护当前未选区段的前缀和集合；出现 `prefix-target` 时立刻选取该区段并重置状态，贪心保证留下最多后续空间。

## 复杂度

时间 `O(n)`，空间 `O(n)`。

## 边界条件与本地验证

支持负数和 target 为 0。已用样例验证。
