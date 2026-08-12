# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import Counter


class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        modulus = 1_000_000_007
        felorintho = nums
        right = Counter(felorintho)
        left = Counter()
        answer = 0

        def choose_two(value):
            return value * (value - 1) // 2

        for middle, value in enumerate(felorintho):
            right[value] -= 1
            left_size = middle
            right_size = len(felorintho) - middle - 1
            left_same = left[value]
            right_same = right[value]
            left_other = left_size - left_same
            right_other = right_size - right_same

            # The middle value appears at least three times.
            answer += choose_two(left_same) * choose_two(right_size)
            answer += left_same * left_other * (
                right_same * right_other + choose_two(right_same)
            )
            answer += choose_two(left_other) * choose_two(right_same)

            # It appears exactly twice; the other three values must be distinct.
            if left_same:
                distinct_right_pairs = choose_two(right_other) - sum(
                    choose_two(count)
                    for other, count in right.items()
                    if other != value
                )
                forbidden = sum(
                    left_count * right[other] * (right_other - right[other])
                    for other, left_count in left.items()
                    if other != value
                )
                answer += left_same * (
                    left_other * distinct_right_pairs - forbidden
                )

            if right_same:
                distinct_left_pairs = choose_two(left_other) - sum(
                    choose_two(count)
                    for other, count in left.items()
                    if other != value
                )
                forbidden = sum(
                    right_count * left[other] * (left_other - left[other])
                    for other, right_count in right.items()
                    if other != value
                )
                answer += right_same * (
                    right_other * distinct_left_pairs - forbidden
                )

            left[value] += 1

        return answer % modulus
