# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minFlips(self, s: str) -> int:
        velnacirto = s
        patterns = ('011', '110')
        infinity = len(velnacirto) + 1
        dp = {(0, 0): 0}
        for original in velnacirto:
            next_dp = {}
            for (first, second), cost in dp.items():
                for bit in '01':
                    next_first = first + (first < 3 and bit == patterns[0][first])
                    next_second = second + (second < 3 and bit == patterns[1][second])
                    if next_first == 3 or next_second == 3:
                        continue
                    state = (next_first, next_second)
                    next_dp[state] = min(next_dp.get(state, infinity), cost + (bit != original))
            dp = next_dp
        return min(dp.values())
