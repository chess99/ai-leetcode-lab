# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        changes = [0] * (k + 2)
        pairs = len(nums) // 2
        for left, right in zip(nums[:pairs], reversed(nums[pairs:])):
            difference = abs(left - right)
            maximum = max(left, right, k - left, k - right)
            changes[0] -= 1
            changes[maximum + 1] += 1
            changes[difference] -= 1
            changes[difference + 1] += 1
        answer = pairs * 2
        current = 0
        for difference in range(k + 1):
            current += changes[difference]
            answer = min(answer, pairs * 2 + current)
        return answer
