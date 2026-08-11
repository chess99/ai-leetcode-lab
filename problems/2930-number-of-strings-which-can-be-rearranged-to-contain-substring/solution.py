# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def stringCount(self, n: int) -> int:
        modulo = 1_000_000_007
        dp = [[[0] * 2 for _ in range(3)] for _ in range(2)]
        dp[0][0][0] = 1
        for _ in range(n):
            next_dp = [[[0] * 2 for _ in range(3)] for _ in range(2)]
            for has_l in range(2):
                for e_count in range(3):
                    for has_t in range(2):
                        value = dp[has_l][e_count][has_t]
                        next_dp[has_l][e_count][has_t] = (next_dp[has_l][e_count][has_t] + 23 * value) % modulo
                        next_dp[1][e_count][has_t] = (next_dp[1][e_count][has_t] + value) % modulo
                        next_dp[has_l][min(2, e_count + 1)][has_t] = (next_dp[has_l][min(2, e_count + 1)][has_t] + value) % modulo
                        next_dp[has_l][e_count][1] = (next_dp[has_l][e_count][1] + value) % modulo
            dp = next_dp
        return dp[1][2][1]
