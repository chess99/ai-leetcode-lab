# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:36Z
# Experiment: ai-leetcode-lab, round 1
from functools import cmp_to_key


class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        mod = 1_000_000_007
        velqoranim = (nums1, nums0)

        def blocks(piece):
            ones, zeros = piece
            result = []
            if ones:
                result.append((1, ones))
            if zeros:
                result.append((0, zeros))
            return result

        def compare(first, second):
            # Compare first + second with second + first without constructing
            # strings whose total length can be large.
            left = blocks(first) + blocks(second)
            right = blocks(second) + blocks(first)
            i = j = 0
            left_remaining = left[0][1]
            right_remaining = right[0][1]
            while i < len(left) and j < len(right):
                if left[i][0] != right[j][0]:
                    return -1 if left[i][0] > right[j][0] else 1
                used = min(left_remaining, right_remaining)
                left_remaining -= used
                right_remaining -= used
                if left_remaining == 0:
                    i += 1
                    if i < len(left):
                        left_remaining = left[i][1]
                if right_remaining == 0:
                    j += 1
                    if j < len(right):
                        right_remaining = right[j][1]
            return 0

        pieces = sorted(zip(nums1, nums0), key=cmp_to_key(compare))
        limit = sum(a + b for a, b in pieces)
        powers = [1] * (limit + 1)
        for i in range(1, limit + 1):
            powers[i] = powers[i - 1] * 2 % mod
        answer = 0
        for ones, zeros in pieces:
            value = (powers[ones] - 1) * powers[zeros] % mod
            answer = (answer * powers[ones + zeros] + value) % mod
        return answer
