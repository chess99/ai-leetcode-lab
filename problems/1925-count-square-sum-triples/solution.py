# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:54:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countTriples(self, n: int) -> int:
        squares = {i*i for i in range(1, n+1)}
        return sum(a*a + b*b in squares for a in range(1,n+1) for b in range(1,n+1))
