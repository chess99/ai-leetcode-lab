# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:14:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [1] * n
        for _ in range(1, m):
            for column in range(1, n):
                paths[column] += paths[column - 1]
        return paths[-1]
