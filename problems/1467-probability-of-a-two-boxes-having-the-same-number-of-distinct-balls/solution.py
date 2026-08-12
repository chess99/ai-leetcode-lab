# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        from math import factorial
        total = sum(balls); all_ways = good = 0
        def dfs(i, left, distinct_left, distinct_right, ways):
            nonlocal all_ways, good
            if i == len(balls):
                if left * 2 == total:
                    all_ways += ways
                    if distinct_left == distinct_right: good += ways
                return
            for taken in range(balls[i] + 1):
                dfs(i + 1, left + taken, distinct_left + (taken > 0), distinct_right + (taken < balls[i]), ways * factorial(balls[i]) // factorial(taken) // factorial(balls[i] - taken))
        dfs(0, 0, 0, 0, 1)
        return good / all_ways
