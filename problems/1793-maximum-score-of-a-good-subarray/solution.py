# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:44Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = right = k
        minimum = answer = nums[k]
        while left > 0 or right + 1 < len(nums):
            if left == 0:
                right += 1
                minimum = min(minimum, nums[right])
            elif right + 1 == len(nums):
                left -= 1
                minimum = min(minimum, nums[left])
            elif nums[left - 1] >= nums[right + 1]:
                left -= 1
                minimum = min(minimum, nums[left])
            else:
                right += 1
                minimum = min(minimum, nums[right])
            answer = max(answer, minimum * (right - left + 1))
        return answer
