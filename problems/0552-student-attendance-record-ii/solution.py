# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:18Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkRecord(self, n: int) -> int:
        modulus = 1_000_000_007
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1
        for _ in range(n):
            following = [[0] * 3 for _ in range(2)]
            for absences in range(2):
                for late in range(3):
                    count = dp[absences][late]
                    following[absences][0] = (following[absences][0] + count) % modulus
                    if absences == 0:
                        following[1][0] = (following[1][0] + count) % modulus
                    if late < 2:
                        following[absences][late + 1] = (following[absences][late + 1] + count) % modulus
            dp = following
        return sum(map(sum, dp)) % modulus
