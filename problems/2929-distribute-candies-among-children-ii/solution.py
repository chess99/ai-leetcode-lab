# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        answer = 0
        for first in range(max(0, n - 2 * limit), min(limit, n) + 1):
            remaining = n - first
            answer += max(0, min(limit, remaining) - max(0, remaining - limit) + 1)
        return answer
