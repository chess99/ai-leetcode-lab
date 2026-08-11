# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:32:58Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        total=0
        while n:n,digit=divmod(n,k);total+=digit
        return total
