# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minOperations(self, n: int) -> int:
        operations = 0
        while n:
            if n == 1:
                return operations + 1
            if n & 1:
                if n & 3 == 3:
                    n += 1
                else:
                    n -= 1
                operations += 1
            else:
                n >>= 1
        return operations
