# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

先把分组编号中的 `k` 项重写：第一组贡献 `k * totalCost`，每增加一个位于 `p` 后的分割点，就额外贡献 `k * suffixCost[p]`。令 `dp[r]` 为覆盖前 `r` 个元素的最小代价，枚举最后一段左端 `l`，加上该段的 `prefixNums[r] * segmentCost(l,r)` 以及新切点贡献即可，消除了分组数这一维。

## 复杂度

时间复杂度 `O(n^2)`，空间复杂度 `O(n)`。

## 边界条件与本地验证

覆盖只有一段、每个元素单独成段及不同切分数。两组官方样例通过，并对小数组枚举全部切分掩码对拍。
