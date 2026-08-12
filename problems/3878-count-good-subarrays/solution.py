# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:29:01Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        qorvanelid = nums
        # For each distinct OR of subarrays ending at the previous position,
        # retain the interval of possible starting indices.  A range is good
        # iff its OR value occurs at some index inside that interval.
        last = {}
        states = []  # (or value, smallest start, largest start)
        answer = 0
        for right, value in enumerate(nums):
            last[value] = right
            merged = [(value, right, right)]
            for current_or, low, high in states:
                next_or = current_or | value
                if merged[-1][0] == next_or:
                    merged[-1] = (next_or, low, merged[-1][2])
                else:
                    merged.append((next_or, low, high))
            states = merged
            for current_or, low, high in states:
                occurrence = last.get(current_or, -1)
                if occurrence >= low:
                    answer += min(high, occurrence) - low + 1
        return answer
