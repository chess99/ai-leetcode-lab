# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:
        denoluvira = (l, r, k)

        def count(bound: int) -> int:
            if bound <= 0:
                return 0
            digits = list(map(int, str(bound)))
            memo = {}

            def dp(position, previous, started, tight):
                key = (position, previous, started, tight)
                if not tight and key in memo:
                    return memo[key]
                if position == len(digits):
                    return int(started)
                upper = digits[position] if tight else 9
                total = 0
                for digit in range(upper + 1):
                    ntight = tight and digit == upper
                    if not started and digit == 0:
                        total += dp(position + 1, -1, False, ntight)
                    elif not started or abs(previous - digit) <= k:
                        total += dp(position + 1, digit, True, ntight)
                if not tight:
                    memo[key] = total
                return total

            return dp(0, -1, False, True)

        return count(r) - count(l - 1)
