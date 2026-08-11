# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        answer = []
        for value in nums:
            answer.append(-1 if value % 2 == 0 else value - ((value + 1 & -(value + 1)) // 2))
        return answer
