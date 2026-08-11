# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:13Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for operations in range(1, 61):
            remaining = num1 - operations * num2
            if remaining >= operations and remaining.bit_count() <= operations:
                return operations
        return -1
