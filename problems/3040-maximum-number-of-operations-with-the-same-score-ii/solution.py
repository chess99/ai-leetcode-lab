# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Revised from the terra-medium candidate after its memory-limit failure.
from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def solve(target: int) -> int:
            # For intervals of the parity of n, keep only the preceding
            # length diagonal. Every transition shortens an interval by 2.
            if n % 2 == 0:
                previous = [0] * (n + 1)  # Empty intervals (length 0).
                first_length = 2
            else:
                previous = [0] * n  # Single-element intervals (length 1).
                first_length = 3

            for length in range(first_length, n + 1, 2):
                current = [0] * (n - length + 1)
                for left in range(n - length + 1):
                    right = left + length - 1
                    best = 0

                    if nums[left] + nums[left + 1] == target:
                        best = 1 + previous[left + 2]
                    if nums[right - 1] + nums[right] == target:
                        best = max(best, 1 + previous[left])
                    if nums[left] + nums[right] == target:
                        best = max(best, 1 + previous[left + 1])

                    current[left] = best
                previous = current

            return previous[0]

        targets = {
            nums[0] + nums[1],
            nums[-2] + nums[-1],
            nums[0] + nums[-1],
        }
        return max(solve(target) for target in targets)
