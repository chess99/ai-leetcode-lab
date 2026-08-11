# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

前缀和支持 O(1) 求平均值。dp[start] 表示当前分组数下从 start 开始的最大平均和；枚举第一组结束位置并接后续最优值，按组数原地更新。

## 复杂度

时间 O(k*n²)，空间 O(n)。

## 边界条件与本地验证

每组至少一个元素；k=1 即全数组平均。本地对示例、k=1 和 k=n 断言，并执行 py_compile。
