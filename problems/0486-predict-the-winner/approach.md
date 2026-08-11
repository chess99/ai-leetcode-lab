# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

令 `dp[left][right]` 表示当前玩家面对子数组 `nums[left:right+1]` 时，自己最多能比对手多得到的分数。若拿左端，净优势为 `nums[left] - dp[left+1][right]`；若拿右端，则为 `nums[right] - dp[left][right-1]`。取两者较大值。

长度为一的区间优势就是该数字。按 `left` 从右向左、`right` 从左向右填表时，可将二维状态压缩到一维：更新前的 `dp[right]` 对应 `dp[left+1][right]`，更新后的 `dp[right-1]` 对应 `dp[left][right-1]`。最终优势非负代表玩家 1 至少战平，题意下即可获胜。

## 复杂度

- 时间 `O(n²)`，会计算所有区间。
- 一维状态数组使用 `O(n)` 额外空间。

## 边界条件与本地验证

- 只有一个数字时，玩家 1 必胜，初始化的一维状态即可得到非负优势。
- 平局也应返回 `True`，最终使用 `>= 0` 判断。
- 元素可以为 `0`，递推仍成立。

本地对题目两个示例、单元素、平局数组和含零数组做最小断言，并执行 `py_compile` 语法检查。
