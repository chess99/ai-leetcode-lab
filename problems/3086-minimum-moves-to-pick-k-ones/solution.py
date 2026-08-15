# AI solution attribution (current candidate)
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Original candidate: Codex Desktop / gpt-5.6-terra / medium
# Experiment: ai-leetcode-lab
from typing import List


class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        positions = [index for index, value in enumerate(nums) if value]

        longest_run = run = 0
        for value in nums:
            if value:
                run += 1
                longest_run = max(longest_run, run)
            else:
                run = 0

        cheap = min(longest_run, 3, k)
        if cheap + maxChanges >= k:
            return max(0, cheap - 1) + 2 * (k - cheap)

        needed = k - maxChanges
        prefix = [0]
        for position in positions:
            prefix.append(prefix[-1] + position)

        best = 10**18
        for left in range(len(positions) - needed + 1):
            right = left + needed
            middle = (left + right - 1) // 2
            median = positions[middle]
            move_left = median * (middle - left) - (prefix[middle] - prefix[left])
            move_right = (prefix[right] - prefix[middle + 1]) - median * (right - middle - 1)
            best = min(best, move_left + move_right + 2 * maxChanges)
        return best
