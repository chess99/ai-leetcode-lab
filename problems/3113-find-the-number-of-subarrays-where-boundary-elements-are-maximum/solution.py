# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        answer = len(nums)
        stack = []
        for value in nums:
            while stack and stack[-1][0] < value:
                stack.pop()
            if stack and stack[-1][0] == value:
                answer += stack[-1][1]
                stack[-1][1] += 1
            else:
                stack.append([value, 1])
        return answer
