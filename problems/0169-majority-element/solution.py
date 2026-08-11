# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:22:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for number in nums:
            if count == 0:
                candidate = number
            count += 1 if number == candidate else -1
        return candidate
