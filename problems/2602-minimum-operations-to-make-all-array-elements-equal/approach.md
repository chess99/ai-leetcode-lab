# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

排序并建立前缀和。对每个查询值 `q`，二分得到不大于 `q` 的分界位置：左侧总操作数为 `q * count - leftSum`，右侧为 `rightSum - q * count`，相加即可。

## 复杂度

预处理为 `O(n log n)` 时间、`O(n)` 空间；每次查询 `O(log n)` 时间。

## 边界条件与本地验证

分界使用右侧二分，使等于查询值的元素归到左侧但贡献为零。查询值小于全部元素或大于全部元素时，一侧自然为空。
