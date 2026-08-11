# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:57:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        candidate = n
        while True:
            product = 1
            for digit in str(candidate):
                product *= int(digit)
            if product % t == 0:
                return candidate
            candidate += 1
