# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:29Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 2:return False
            n //= 3
        return True
