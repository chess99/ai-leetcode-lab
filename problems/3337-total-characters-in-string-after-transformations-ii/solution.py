# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        modulus = 1_000_000_007
        matrix = [[0] * 26 for _ in range(26)]
        for source, count in enumerate(nums):
            for step in range(1, count + 1):
                matrix[(source + step) % 26][source] += 1

        def multiply(first, second):
            result = [[0] * 26 for _ in range(26)]
            for row in range(26):
                for middle in range(26):
                    if first[row][middle]:
                        coefficient = first[row][middle]
                        for column in range(26):
                            result[row][column] = (result[row][column]
                                                   + coefficient * second[middle][column]) % modulus
            return result

        result = [[int(row == column) for column in range(26)] for row in range(26)]
        while t:
            if t & 1:
                result = multiply(result, matrix)
            matrix = multiply(matrix, matrix)
            t >>= 1

        counts = [0] * 26
        for character in s:
            counts[ord(character) - 97] += 1
        return sum(result[row][column] * counts[column]
                   for row in range(26) for column in range(26)) % modulus
