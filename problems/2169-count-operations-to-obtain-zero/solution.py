# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:18:02Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 and num2:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            count += 1
        return count
