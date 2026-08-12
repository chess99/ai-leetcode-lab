# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

动态规划按可用地毯数逐层推进。`dp[i]` 表示覆盖前 `i` 块砖后的最少可见白砖：不在第 `i` 块处结束地毯时，由 `dp[i-1]` 加当前砖颜色；使用一条地毯覆盖末尾至多 `carpetLen` 块时，转移自上一层的 `dp[max(0,i-carpetLen)]`。滚动两层即可。

## 复杂度

时间 `O(numCarpets * floor.length)`，空间 `O(floor.length)`。

## 边界条件与本地验证

地毯允许重叠或伸出已处理前缀，地毯总覆盖能力足够时答案为 0。题面样例得到 `2、0`；长度不超过 8 的随机地板枚举所有地毯起点组合，与 DP 对拍。
