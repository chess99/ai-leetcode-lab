# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def racecar(self, target: int) -> int:
        dp=[0]*(target+1)
        for distance in range(1,target+1):
            moves=distance.bit_length();full=(1<<moves)-1
            if full==distance:dp[distance]=moves;continue
            dp[distance]=moves+1+dp[full-distance]
            previous=(1<<(moves-1))-1
            for reverse in range(moves-1):
                backward=(1<<reverse)-1
                remaining=distance-(previous-backward)
                dp[distance]=min(dp[distance],moves+reverse+1+dp[remaining])
        return dp[target]
