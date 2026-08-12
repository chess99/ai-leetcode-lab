# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        parvostine = nums
        stack = []
        answer = 0
        for right, value in enumerate(parvostine):
            while stack and parvostine[stack[-1]] < value:
                left = stack.pop()
                if right - left >= 2:
                    answer += 1
            if stack and right - stack[-1] >= 2:
                answer += 1
            stack.append(right)
        return answer
