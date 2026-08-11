# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:54:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        previous=-k-1
        for index,value in enumerate(nums):
            if value:
                if index-previous<=k:return False
                previous=index
        return True
