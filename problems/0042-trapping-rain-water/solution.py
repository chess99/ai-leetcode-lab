# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = answer = 0
        while left <= right:
            if left_max <= right_max:
                left_max = max(left_max, height[left])
                answer += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                answer += right_max - height[right]
                right -= 1
        return answer
