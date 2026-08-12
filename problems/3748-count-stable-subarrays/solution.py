# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        lamorvick = (nums, queries)
        n = len(nums)
        run_id = [0] * n
        starts = []
        ends = []
        start = 0
        run = 0
        for index in range(1, n + 1):
            if index < n and nums[index - 1] <= nums[index]:
                continue
            starts.append(start)
            ends.append(index - 1)
            for position in range(start, index):
                run_id[position] = run
            run += 1
            start = index

        prefix = [0]
        for left, right in zip(starts, ends):
            length = right - left + 1
            prefix.append(prefix[-1] + length * (length + 1) // 2)

        answer = []
        for left, right in queries:
            first = run_id[left]
            last = run_id[right]
            if first == last:
                length = right - left + 1
                answer.append(length * (length + 1) // 2)
                continue
            left_length = ends[first] - left + 1
            right_length = right - starts[last] + 1
            total = left_length * (left_length + 1) // 2
            total += right_length * (right_length + 1) // 2
            total += prefix[last] - prefix[first + 1]
            answer.append(total)
        return answer
