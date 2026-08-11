# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:25Z
# Experiment: ai-leetcode-lab, round 1


class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0

        minimum = 10 if k == 0 else k
        for count in range(1, 11):
            if count * minimum <= num and (count * k) % 10 == num % 10:
                return count
        return -1
