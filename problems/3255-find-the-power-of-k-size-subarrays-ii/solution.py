# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        answer = []
        length = 0
        for index, value in enumerate(nums):
            length = length + 1 if index and value == nums[index - 1] + 1 else 1
            if index >= k - 1:
                answer.append(value if length >= k else -1)
        return answer
