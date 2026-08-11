# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        position = 1
        operations = 0

        while True:
            if position % 2 == 0:
                position //= 2
            else:
                position = n // 2 + (position - 1) // 2
            operations += 1
            if position == 1:
                return operations
