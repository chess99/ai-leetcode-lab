# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:16:01Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        size = len(nums)
        tree = [0] * (size + 1)

        def is_peak(index):
            return (0 < index < size - 1
                    and nums[index] > nums[index - 1]
                    and nums[index] > nums[index + 1])

        def add(index, difference):
            index += 1
            while index <= size:
                tree[index] += difference
                index += index & -index

        def prefix(end):
            total = 0
            while end:
                total += tree[end]
                end -= end & -end
            return total

        peaks = [False] * size
        for index in range(1, size - 1):
            peaks[index] = is_peak(index)
            if peaks[index]:
                add(index, 1)

        answer = []
        for kind, first, second in queries:
            if kind == 1:
                left, right = first, second
                if right - left < 2:
                    answer.append(0)
                else:
                    answer.append(prefix(right) - prefix(left + 1))
            else:
                index, value = first, second
                nums[index] = value
                for affected in range(max(1, index - 1), min(size - 1, index + 2)):
                    updated = is_peak(affected)
                    if updated != peaks[affected]:
                        add(affected, 1 if updated else -1)
                        peaks[affected] = updated
        return answer
