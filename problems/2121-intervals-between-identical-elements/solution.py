# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:26Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        answer = [0] * len(arr)
        counts = defaultdict(int)
        index_sums = defaultdict(int)

        for index, value in enumerate(arr):
            answer[index] += index * counts[value] - index_sums[value]
            counts[value] += 1
            index_sums[value] += index

        counts.clear()
        index_sums.clear()

        for index in range(len(arr) - 1, -1, -1):
            value = arr[index]
            answer[index] += index_sums[value] - index * counts[value]
            counts[value] += 1
            index_sums[value] += index

        return answer
