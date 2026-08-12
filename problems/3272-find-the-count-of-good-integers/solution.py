# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:31Z
# Experiment: ai-leetcode-lab, round 1
from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        half = (n + 1) // 2
        signatures = set()
        for prefix in range(10 ** (half - 1), 10 ** half):
            left = str(prefix)
            palindrome = left + (left[:-1] if n & 1 else left)[::-1]
            if int(palindrome) % k == 0:
                signatures.add(tuple(sorted(palindrome)))

        answer = 0
        for signature in signatures:
            counts = [signature.count(str(digit)) for digit in range(10)]
            ways = factorial(n)
            for count in counts:
                ways //= factorial(count)
            if counts[0]:
                leading_zero = factorial(n - 1)
                leading_zero //= factorial(counts[0] - 1)
                for count in counts[1:]:
                    leading_zero //= factorial(count)
                ways -= leading_zero
            answer += ways
        return answer
