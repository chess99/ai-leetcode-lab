# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:37:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None
        for number in nums:
            if number in (first, second, third):
                continue
            if first is None or number > first:
                first, second, third = number, first, second
            elif second is None or number > second:
                second, third = number, second
            elif third is None or number > third:
                third = number
        return third if third is not None else first
