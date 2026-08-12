# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        half = (n + 1) // 2
        powers = [1] * n
        for index in range(1, n):
            powers[index] = powers[index - 1] * 10 % k

        weights = [0] * half
        for index in range(half):
            mirror = n - 1 - index
            weights[index] = powers[index] if index == mirror else (powers[index] + powers[mirror]) % k

        reachable = [0] * (half + 1)
        reachable[half] = 1
        for index in range(half - 1, -1, -1):
            mask = 0
            first_digit = 1 if index == 0 else 0
            next_mask = reachable[index + 1]
            for digit in range(first_digit, 10):
                add = digit * weights[index] % k
                for remainder in range(k):
                    if next_mask >> remainder & 1:
                        mask |= 1 << ((add + remainder) % k)
            reachable[index] = mask

        digits = ['0'] * n
        remainder = 0
        for index in range(half):
            lower = 1 if index == 0 else 0
            for digit in range(9, lower - 1, -1):
                new_remainder = (remainder + digit * weights[index]) % k
                needed = (-new_remainder) % k
                if reachable[index + 1] >> needed & 1:
                    digits[index] = digits[n - 1 - index] = str(digit)
                    remainder = new_remainder
                    break
        return ''.join(digits)
