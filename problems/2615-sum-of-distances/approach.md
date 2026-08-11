# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

按数值收集其出现下标。对于同一组已递增的下标，在位置 `i` 处，左侧贡献为 `i * leftCount - leftSum`，右侧贡献为 `rightSum - i * rightCount`。扫描组内下标并维护左侧和即可在常数时间求每个答案。

## 复杂度

时间 `O(n)`，分组及答案使用 `O(n)` 空间。

## 边界条件与本地验证

只出现一次的数左右两侧均为空，答案自然为零。下标按原数组从左到右加入列表，已天然有序。
