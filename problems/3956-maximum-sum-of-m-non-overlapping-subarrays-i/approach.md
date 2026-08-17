# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 接手 Profile：sol-medium（Codex Desktop / gpt-5.6-sol / medium）

## Terra 失败与根因

Terra 版本在第 `k` 层使用 `nd[i] = max(nd[i - 1], dp[i], ...)`。其中 `dp[i]`
会把初始的“选择 0 段、总和为 0”一路带到每一层，所以最终状态实际允许不选择任何
子数组。这与题目要求的“至少一个”冲突。远判反例
`nums = [-3,-4,-1], m = 2, l = 1, r = 2` 因而返回 `0`，正确答案应为 `-1`。

## sol-medium 新思路：恰好段数 DP + 单调队列

令 `previous[i]` 表示只考虑 `nums[:i]`、**恰好**选择 `k-1` 个合法子数组时的
最大和；当前层 `current[i]` 对应恰好选择 `k` 段。新一段以 `end` 为右端点（右开）
并从 `start` 开始时，必须满足

```text
end - r <= start <= end - l
```

转移为

```text
current[end] = max(
    current[end - 1],
    prefix[end] + max(previous[start] - prefix[start])
)
```

窗口中的 `start` 随 `end` 单调右移，用单调递减队列维护
`previous[start] - prefix[start]` 的最大值。不可达的 `previous[start]` 不入队，避免
从哨兵值伪造可达状态。

第 0 层在任意前缀中恰好选择 0 段的值均为 0。之后每层只从上一层增加一段，绝不
跨层继承 `previous[i]`。最终对恰好选择 `1..min(m, n // l)` 段的答案取最大值，既
支持“至多 `m` 段”，又严格保证“至少一段”。题面要求的变量 `qerunavilo` 在函数中部
保存了完整输入。

## 正确性证明

对段数 `k` 归纳。第 0 层显然正确：任意前缀恰好选 0 段的唯一总和是 0。

假设 `previous` 正确表示恰好 `k-1` 段。对 `current[end]`，任一最优方案分两类：

1. 不使用 `nums[end-1]`，它完整包含在 `nums[:end-1]`，值为 `current[end-1]`；
2. 最后一段恰好在 `end` 结束。设其起点为 `start`，长度约束等价于上述滑动窗口，
   前 `k-1` 段必须位于 `nums[:start]`，最优值为
   `previous[start] + prefix[end] - prefix[start]`。

转移枚举了第二类的全部合法起点，并与第一类取最大，因此 `current[end]` 正确。
归纳得每层均正确。最后在所有允许的正段数中取最大值，故返回值恰为题目要求的最优解。

## 复杂度

最多计算 `min(m, n // l)` 层，每层线性扫描。时间复杂度
`O(n * min(m, n // l))`，空间复杂度 `O(n)`。

## 边界条件与本地验证

- 全负数组仍必须选择至少一段，不能用 0 覆盖负答案；
- `l = r` 时队列窗口退化为唯一合法起点；
- `m > n // l` 时跳过不可能存在的额外层；
- 数值范围使用 Python 整数，覆盖总和绝对值达到 `10^12` 的情况。
