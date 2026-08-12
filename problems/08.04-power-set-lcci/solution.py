# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        for value in nums:
            answer += [subset + [value] for subset in answer]
        return answer
