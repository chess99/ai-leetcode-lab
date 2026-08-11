# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:28Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        positions = defaultdict(list)
        for index, value in enumerate(nums):
            positions[value].append(index)
        answer = [0] * len(nums)
        for indices in positions.values():
            total = sum(indices)
            left_sum = 0
            size = len(indices)
            for order, index in enumerate(indices):
                right_sum = total - left_sum - index
                answer[index] = index * order - left_sum + right_sum - index * (size - order - 1)
                left_sum += index
        return answer
