# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        from collections import Counter
        from math import isqrt

        rows, cols = len(mat), len(mat[0])
        counts = Counter()
        for row in range(rows):
            for col in range(cols):
                for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                    value, r, c = 0, row, col
                    while 0 <= r < rows and 0 <= c < cols:
                        value = value * 10 + mat[r][c]
                        if value > 10:
                            counts[value] += 1
                        r += dr
                        c += dc

        def is_prime(value: int) -> bool:
            if value < 2:
                return False
            for divisor in range(2, isqrt(value) + 1):
                if value % divisor == 0:
                    return False
            return True

        answer, best_count = -1, 0
        for value, count in counts.items():
            if is_prime(value) and (count > best_count or (count == best_count and value > answer)):
                answer, best_count = value, count
        return answer
