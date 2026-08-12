# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        timberavos = (nums, k)
        values = sorted(set(nums))
        rank = {value: index + 1 for index, value in enumerate(values)}
        bit = [0] * (len(values) + 1)

        def add(index: int, delta: int) -> None:
            while index < len(bit):
                bit[index] += delta
                index += index & -index

        def prefix(index: int) -> int:
            result = 0
            while index:
                result += bit[index]
                index -= index & -index
            return result

        inversions = 0
        for index in range(k):
            current_rank = rank[nums[index]]
            inversions += index - prefix(current_rank)
            add(current_rank, 1)
        answer = inversions

        for right in range(k, len(nums)):
            outgoing_rank = rank[nums[right - k]]
            add(outgoing_rank, -1)
            inversions -= prefix(outgoing_rank - 1)

            incoming_rank = rank[nums[right]]
            inversions += (k - 1) - prefix(incoming_rank)
            add(incoming_rank, 1)
            answer = min(answer, inversions)
        return answer
