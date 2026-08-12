# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        for number in nums:
            answer += [subset + [number] for subset in answer]
        return answer
