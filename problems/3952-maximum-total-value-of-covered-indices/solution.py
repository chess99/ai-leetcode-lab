# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        velunqari = (nums, s)
        answer = 0
        index = 0
        while index < len(s):
            if s[index] == '0':
                index += 1
                continue
            left = index
            while index + 1 < len(s) and s[index + 1] == '1':
                index += 1
            right = index
            if left == 0:
                answer += sum(nums[:right + 1])
            else:
                values = nums[left - 1:right + 1]
                answer += sum(values) - min(values)
            index += 1
        return answer
