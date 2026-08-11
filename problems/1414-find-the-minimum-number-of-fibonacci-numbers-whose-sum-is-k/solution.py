# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:49:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        first, second = 1, 1
        while second <= k:
            first, second = second, first + second
        count = 0
        while k:
            if first <= k:
                k -= first
                count += 1
            first, second = second - first, first
        return count
