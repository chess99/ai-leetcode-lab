# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:56:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isThree(self, n: int) -> bool:
        root = int(n ** 0.5)
        if root * root != n or root < 2:
            return False
        return all(root % divisor for divisor in range(2, int(root ** 0.5) + 1))
