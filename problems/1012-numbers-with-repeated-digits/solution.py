# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        digits = list(map(int, str(n + 1)))

        def permutations(available, length):
            result = 1
            for offset in range(length):
                result *= available - offset
            return result

        unique = 0
        for length in range(1, len(digits)):
            unique += 9 * permutations(9, length - 1)
        used = set()
        for index, digit in enumerate(digits):
            for candidate in range(0 if index else 1, digit):
                if candidate not in used:
                    unique += permutations(10 - len(used) - 1,
                                           len(digits) - index - 1)
            if digit in used:
                break
            used.add(digit)
        return n - unique
