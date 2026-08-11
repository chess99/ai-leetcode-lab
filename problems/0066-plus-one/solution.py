# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:11:37Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for index in range(len(digits) - 1, -1, -1):
            if digits[index] < 9:
                digits[index] += 1
                return digits
            digits[index] = 0
        return [1] + digits
