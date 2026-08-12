# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:58Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        modulus = 1_000_000_007
        end_zero = [[0] * (one + 1) for _ in range(zero + 1)]
        end_one = [[0] * (one + 1) for _ in range(zero + 1)]
        for used_zero in range(1, min(zero, limit) + 1):
            end_zero[used_zero][0] = 1
        for used_one in range(1, min(one, limit) + 1):
            end_one[0][used_one] = 1
        for used_zero in range(1, zero + 1):
            for used_one in range(1, one + 1):
                end_zero[used_zero][used_one] = (
                    end_zero[used_zero - 1][used_one]
                    + end_one[used_zero - 1][used_one]) % modulus
                if used_zero > limit:
                    end_zero[used_zero][used_one] -= end_one[used_zero - limit - 1][used_one]
                end_zero[used_zero][used_one] %= modulus

                end_one[used_zero][used_one] = (
                    end_one[used_zero][used_one - 1]
                    + end_zero[used_zero][used_one - 1]) % modulus
                if used_one > limit:
                    end_one[used_zero][used_one] -= end_zero[used_zero][used_one - limit - 1]
                end_one[used_zero][used_one] %= modulus
        return (end_zero[zero][one] + end_one[zero][one]) % modulus
