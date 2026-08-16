# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Handoff from: terra-medium (gpt-5.6-terra / medium)
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ravolthine = fruits
        answer = sum(ravolthine[i][i] for i in range(n))
        unreachable = -1

        def collect_side(transposed: bool) -> int:
            # 转置后，左下角孩子与右上角孩子具有完全相同的移动方式。
            dp = [unreachable] * n
            dp[n - 1] = (
                ravolthine[n - 1][0]
                if transposed
                else ravolthine[0][n - 1]
            )

            for row in range(1, n):
                next_dp = [unreachable] * n
                # 两个下界分别来自“从起点至多左移 row 格”和
                # “剩余步数必须足够到达终点”。
                for col in range(max(row, n - 1 - row), n):
                    best = dp[col]
                    if col > 0:
                        best = max(best, dp[col - 1])
                    if col + 1 < n:
                        best = max(best, dp[col + 1])
                    if best == unreachable:
                        continue

                    # 主对角线上的水果已经由第一个孩子收集。
                    value = 0
                    if row != col:
                        value = (
                            ravolthine[col][row]
                            if transposed
                            else ravolthine[row][col]
                        )
                    next_dp[col] = best + value
                dp = next_dp

            return dp[n - 1]

        return answer + collect_side(False) + collect_side(True)
