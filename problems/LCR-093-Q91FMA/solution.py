# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        positions = {value: index for index, value in enumerate(arr)}
        lengths = {}
        answer = 0
        for second in range(len(arr)):
            for third in range(second + 1, len(arr)):
                previous_value = arr[third] - arr[second]
                if previous_value >= arr[second]:
                    continue
                first = positions.get(previous_value)
                if first is not None:
                    length = lengths.get((first, second), 2) + 1
                    lengths[second, third] = length
                    answer = max(answer, length)
        return answer
