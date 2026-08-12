# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:19Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        answer = []
        path = []

        def backtrack() -> None:
            if len(path) == len(nums):
                answer.append(path[:])
                return
            for number in counts:
                if counts[number] == 0:
                    continue
                counts[number] -= 1
                path.append(number)
                backtrack()
                path.pop()
                counts[number] += 1

        backtrack()
        return answer
