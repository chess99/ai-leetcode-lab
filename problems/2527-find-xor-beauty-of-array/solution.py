# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        answer = 0
        for value in nums:
            answer ^= value
        return answer
