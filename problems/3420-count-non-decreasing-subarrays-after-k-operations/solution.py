# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:13Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        # Blocks are the prefix maxima of the current [left, right] window.
        # Each block stores (raised_value, number_of_positions).
        blocks = deque()
        left = len(nums) - 1
        right = len(nums) - 1
        cost = 0
        answer = 0

        for left in range(len(nums) - 1, -1, -1):
            value = nums[left]
            count = 1
            while blocks and blocks[0][0] < value:
                old, amount = blocks.popleft()
                cost += (value - old) * amount
                count += amount
            blocks.appendleft((value, count))

            while cost > k:
                raised, amount = blocks[-1]
                cost -= raised - nums[right]
                if amount == 1:
                    blocks.pop()
                else:
                    blocks[-1] = (raised, amount - 1)
                right -= 1
            answer += right - left + 1
        return answer
