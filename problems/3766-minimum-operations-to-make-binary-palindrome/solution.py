# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from bisect import bisect_left


class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        ravineldor = nums
        upper = max(ravineldor) * 2 + 1
        palindromes = [value for value in range(1, upper + 1)
                       if (binary := bin(value)[2:]) == binary[::-1]]
        answer = []
        for value in ravineldor:
            index = bisect_left(palindromes, value)
            distance = palindromes[index] - value if index < len(palindromes) else upper
            if index:
                distance = min(distance, value - palindromes[index - 1])
            answer.append(distance)
        return answer
