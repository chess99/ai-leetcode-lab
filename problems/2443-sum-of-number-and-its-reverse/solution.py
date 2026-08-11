# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:18Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        return any(x + int(str(x)[::-1]) == num for x in range(num + 1))
