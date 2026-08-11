# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:31:19Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return sum(a+b+c==n for a in range(min(limit,n)+1) for b in range(min(limit,n-a)+1) for c in range(min(limit,n-a-b)+1))
