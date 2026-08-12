# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        melidroni = (num1, num2)

        def count_up_to(limit: int) -> int:
            if limit <= 0:
                return 0
            digits = list(map(int, str(limit)))
            # (tight, started, previous-previous, previous) -> (数量, 波动和)
            dp = {(True, False, -1, -1): (1, 0)}
            for bound in digits:
                next_dp = {}
                for (tight, started, older, previous), (count, total) in dp.items():
                    upper = bound if tight else 9
                    for digit in range(upper + 1):
                        new_tight = tight and digit == upper
                        if not started and digit == 0:
                            key = (new_tight, False, -1, -1)
                            old_count, old_total = next_dp.get(key, (0, 0))
                            next_dp[key] = (old_count + count, old_total + total)
                            continue
                        extra = int(older != -1 and
                                    ((previous > older and previous > digit) or
                                     (previous < older and previous < digit)))
                        key = (new_tight, True, previous, digit)
                        old_count, old_total = next_dp.get(key, (0, 0))
                        next_dp[key] = (old_count + count, old_total + total + extra * count)
                dp = next_dp
            return sum(total for (_, started, _, _), (_, total) in dp.items() if started)

        return count_up_to(num2) - count_up_to(num1 - 1)
