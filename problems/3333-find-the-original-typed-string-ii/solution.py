# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:35Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        modulus = 1_000_000_007
        runs = []
        for character in word:
            if not runs or character != runs[-1][0]:
                runs.append([character, 1])
            else:
                runs[-1][1] += 1
        lengths = [length for _, length in runs]
        total = 1
        for length in lengths:
            total = total * length % modulus
        if len(lengths) >= k:
            return total

        dp = [0] * k
        dp[0] = 1
        for maximum in lengths:
            next_dp = [0] * k
            window = 0
            for length in range(1, k):
                window = (window + dp[length - 1]) % modulus
                if length - maximum - 1 >= 0:
                    window = (window - dp[length - maximum - 1]) % modulus
                next_dp[length] = window
            dp = next_dp
        return (total - sum(dp)) % modulus
