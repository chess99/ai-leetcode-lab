# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:10:29Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(value for value in range(1,n+1) if value%3==0 or value%5==0 or value%7==0)
