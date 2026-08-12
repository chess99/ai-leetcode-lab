# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        height_count = n + 1
        prefix = [[0] * height_count for _ in range(n)]
        for col in range(n):
            for row in range(n):
                prefix[col][row + 1] = prefix[col][row] + grid[row][col]

        negative = -1
        dp = [[negative] * height_count for _ in range(height_count)]
        for first_height in range(height_count):
            dp[0][first_height] = 0

        for col in range(n - 1):
            new = [[negative] * height_count for _ in range(height_count)]
            sums = prefix[col]
            for center in range(height_count):
                before = [negative] * height_count
                after = [negative] * (height_count + 1)

                best = negative
                for left in range(height_count):
                    best = max(best, dp[left][center])
                    before[left] = best

                best = negative
                for left in range(height_count - 1, -1, -1):
                    score = sums[left] - sums[center] if left > center else 0
                    if dp[left][center] >= 0:
                        best = max(best, dp[left][center] + score)
                    after[left] = best

                for right in range(height_count):
                    score = sums[right] - sums[center] if right > center else 0
                    value = before[right] + score if before[right] >= 0 else negative
                    if right + 1 < height_count:
                        value = max(value, after[right + 1])
                    new[center][right] = value
            dp = new

        answer = 0
        sums = prefix[n - 1]
        for left in range(height_count):
            for center in range(height_count):
                if dp[left][center] < 0:
                    continue
                score = sums[left] - sums[center] if left > center else 0
                answer = max(answer, dp[left][center] + score)
        return answer
