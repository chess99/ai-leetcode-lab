# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

设最小组大小为 `size`，所有组大小只能是 `size` 或 `size+1`。从最小频次向下枚举最大的可行 `size`；对频次 `count`，所需组数为 `ceil(count/(size+1))`，且这些组最多容量不能小于 count。首个可行 size 给出最少组数。

## 复杂度

时间 `O(n + f * u)`，其中 `f` 为最小频次、`u` 为不同值数；空间 `O(u)`。

## 边界条件与本地验证

单个元素频次使 size 为 1；所有频次都必须同时满足可行性。
