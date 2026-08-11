# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        order = sorted(range(len(nums)), key=lambda index: nums[index])
        marked = [False] * len(nums)
        remaining = sum(nums)
        pointer = 0
        answer = []
        for index, count in queries:
            if not marked[index]:
                marked[index] = True
                remaining -= nums[index]
            while count and pointer < len(nums):
                candidate = order[pointer]
                pointer += 1
                if not marked[candidate]:
                    marked[candidate] = True
                    remaining -= nums[candidate]
                    count -= 1
            answer.append(remaining)
        return answer
