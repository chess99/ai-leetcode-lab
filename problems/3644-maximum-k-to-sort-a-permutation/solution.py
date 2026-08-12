# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        answer = -1
        for index, value in enumerate(nums):
            if index != value:
                answer = value if answer == -1 else answer & value
        return 0 if answer == -1 else answer
