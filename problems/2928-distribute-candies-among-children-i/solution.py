# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:31:19Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0
        for first in range(min(limit, n) + 1):
            for second in range(min(limit, n - first) + 1):
                third = n - first - second
                if third <= limit:
                    result += 1
        return result
