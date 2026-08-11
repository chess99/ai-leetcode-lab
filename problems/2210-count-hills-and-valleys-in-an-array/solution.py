# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:19:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr = [nums[0]]
        for value in nums[1:]:
            if value != arr[-1]: arr.append(value)
        return sum((arr[i] > arr[i-1] and arr[i] > arr[i+1]) or (arr[i] < arr[i-1] and arr[i] < arr[i+1]) for i in range(1, len(arr)-1))
