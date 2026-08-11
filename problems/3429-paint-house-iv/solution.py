# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        inf = 10**30
        dp = [[inf] * 3 for _ in range(3)]
        for left_color in range(3):
            for right_color in range(3):
                if left_color != right_color:
                    dp[left_color][right_color] = cost[0][left_color] + cost[-1][right_color]

        for left in range(1, n // 2):
            right = n - 1 - left
            nxt = [[inf] * 3 for _ in range(3)]
            for old_left in range(3):
                for old_right in range(3):
                    for left_color in range(3):
                        if left_color == old_left:
                            continue
                        for right_color in range(3):
                            if right_color != old_right and right_color != left_color:
                                nxt[left_color][right_color] = min(nxt[left_color][right_color], dp[old_left][old_right] + cost[left][left_color] + cost[right][right_color])
            dp = nxt
        return min(map(min, dp))
