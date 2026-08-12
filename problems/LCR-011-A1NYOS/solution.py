# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = {0: -1}
        balance = answer = 0
        for index, value in enumerate(nums):
            balance += 1 if value else -1
            if balance in first:
                answer = max(answer, index - first[balance])
            else:
                first[balance] = index
        return answer
