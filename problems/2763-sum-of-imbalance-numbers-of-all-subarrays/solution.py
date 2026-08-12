# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        answer = 0
        for left in range(len(nums)):
            seen = {nums[left]}
            imbalance = 0
            for right in range(left + 1, len(nums)):
                value = nums[right]
                if value not in seen:
                    imbalance += 1
                    if value - 1 in seen:
                        imbalance -= 1
                    if value + 1 in seen:
                        imbalance -= 1
                    seen.add(value)
                answer += imbalance
        return answer
