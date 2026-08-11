# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:28Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        largest_by_digit_sum = {}
        answer = -1

        for number in nums:
            digit_sum = sum(int(digit) for digit in str(number))
            if digit_sum in largest_by_digit_sum:
                answer = max(answer, number + largest_by_digit_sum[digit_sum])
            largest_by_digit_sum[digit_sum] = max(
                largest_by_digit_sum.get(digit_sum, 0), number
            )

        return answer
