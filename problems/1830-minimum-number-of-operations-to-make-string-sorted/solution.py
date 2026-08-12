# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:47Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def makeStringSorted(self, s: str) -> int:
        modulus = 1_000_000_007
        size = len(s)
        factorial = [1] * (size + 1)
        for value in range(1, size + 1):
            factorial[value] = factorial[value - 1] * value % modulus
        inverse_factorial = [1] * (size + 1)
        inverse_factorial[size] = pow(factorial[size], modulus - 2, modulus)
        for value in range(size, 0, -1):
            inverse_factorial[value - 1] = inverse_factorial[value] * value % modulus

        counts = Counter(s)
        answer = 0
        for index, char in enumerate(s):
            remaining = size - index - 1
            smaller = sum(counts[candidate] for candidate in counts
                          if candidate < char)
            arrangements = smaller * factorial[remaining] % modulus
            for count in counts.values():
                arrangements = arrangements * inverse_factorial[count] % modulus
            answer = (answer + arrangements) % modulus
            counts[char] -= 1
        return answer
