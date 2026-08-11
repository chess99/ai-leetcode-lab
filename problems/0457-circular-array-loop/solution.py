# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:06:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        size = len(nums)

        def next_index(index: int) -> int:
            return (index + nums[index]) % size

        for start in range(size):
            direction = nums[start] > 0
            slow = fast = start

            while (nums[slow] > 0) == direction and (nums[fast] > 0) == direction:
                fast_next = next_index(fast)
                if (nums[fast_next] > 0) != direction:
                    break

                slow = next_index(slow)
                fast = next_index(fast_next)
                if slow == fast:
                    if slow != next_index(slow):
                        return True
                    break

        return False
