# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:06:56Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        operations = 0
        while target > startValue:
            operations += 1
            if target % 2:
                target += 1
            else:
                target //= 2
        return operations + startValue - target
