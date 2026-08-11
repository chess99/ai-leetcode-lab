# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        zeros = [-1] + [index for index, char in enumerate(s) if char == '0'] + [len(s)]
        answer = 0
        for left, right in zip(zeros, zeros[1:]):
            length = right - left - 1
            answer += length * (length + 1) // 2

        def count_pairs(a: int, b: int, c: int, d: int, needed: int) -> int:
            total = 0
            full_end = min(b, c - needed + 1)
            if full_end >= a:
                total += (full_end - a + 1) * (d - c + 1)
            start = max(a, c - needed + 2)
            end = min(b, d - needed + 1)
            if start <= end:
                count = end - start + 1
                total += count * (d - needed + 2) - (start + end) * count // 2
            return total

        max_zeros = int(len(s) ** 0.5)
        for count in range(1, max_zeros + 1):
            needed = count * count + count
            for first in range(1, len(zeros) - count):
                answer += count_pairs(zeros[first - 1] + 1, zeros[first], zeros[first + count - 1], zeros[first + count] - 1, needed)
        return answer
