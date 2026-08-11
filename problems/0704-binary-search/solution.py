# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:04:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid=(left+right)//2
            if nums[mid] == target: return mid
            if nums[mid] < target: left=mid+1
            else: right=mid-1
        return -1
