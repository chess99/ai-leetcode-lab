# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:20Z
# Experiment: ai-leetcode-lab, round 1
from math import comb
from typing import List


class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        mavoduteru = nums
        mod = 1_000_000_007
        dp = {(0, 0, 0): 1}  # (chosen count, binary carry, set bits)

        for value in mavoduteru:
            powers = [1] * (m + 1)
            for count in range(1, m + 1):
                powers[count] = powers[count - 1] * value % mod

            next_dp = {}
            for (chosen, carry, bits), ways in dp.items():
                remaining = m - chosen
                for count in range(remaining + 1):
                    total = carry + count
                    next_bits = bits + (total & 1)
                    if next_bits > k:
                        continue
                    state = (chosen + count, total >> 1, next_bits)
                    contribution = (ways * comb(remaining, count)
                                    * powers[count]) % mod
                    next_dp[state] = (next_dp.get(state, 0)
                                      + contribution) % mod
            dp = next_dp

        answer = 0
        for (chosen, carry, bits), ways in dp.items():
            if chosen == m and bits + carry.bit_count() == k:
                answer = (answer + ways) % mod
        return answer
