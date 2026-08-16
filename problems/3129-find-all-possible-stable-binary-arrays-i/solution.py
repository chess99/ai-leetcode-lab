# Original candidate attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:38Z
#
# Current candidate attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        modulus = 1_000_000_007

        def bounded_compositions(total: int) -> list[int]:
            """ways[parts]: ordered positive splits of total, each at most limit."""
            ways = [0] * (total + 1)
            previous = [0] * (total + 1)
            previous[0] = 1

            for parts in range(1, total + 1):
                current = [0] * (total + 1)
                window = 0
                for used in range(1, total + 1):
                    window += previous[used - 1]
                    if used - limit - 1 >= 0:
                        window -= previous[used - limit - 1]
                    current[used] = window % modulus
                ways[parts] = current[total]
                previous = current

            return ways

        zero_runs = bounded_compositions(zero)
        one_runs = bounded_compositions(one)
        answer = 0

        # Equal run counts allow either starting bit.
        for runs in range(1, min(zero, one) + 1):
            answer += 2 * zero_runs[runs] * one_runs[runs]

        # If one bit has one extra run, it must occupy both ends.
        for zero_count in range(1, zero + 1):
            one_count = zero_count - 1
            if one_count <= one:
                answer += zero_runs[zero_count] * one_runs[one_count]

        for one_count in range(1, one + 1):
            zero_count = one_count - 1
            if zero_count <= zero:
                answer += zero_runs[zero_count] * one_runs[one_count]

        return answer % modulus
