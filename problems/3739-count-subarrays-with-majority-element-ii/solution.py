# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        melvarion = (nums, target)
        n = len(nums)
        size = 2 * n + 3
        offset = n + 1
        bit = [0] * (size + 1)

        def add(index: int) -> None:
            index += offset
            while index <= size:
                bit[index] += 1
                index += index & -index

        def prefix_count(index: int) -> int:
            index += offset
            result = 0
            while index > 0:
                result += bit[index]
                index -= index & -index
            return result

        prefix = 0
        answer = 0
        add(0)
        for value in nums:
            prefix += 1 if value == target else -1
            answer += prefix_count(prefix - 1)
            add(prefix)
        return answer
