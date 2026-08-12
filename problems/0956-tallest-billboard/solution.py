# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:04Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp={0:0}
        for rod in rods:
            for diff,height in list(dp.items()):
                dp[diff+rod]=max(dp.get(diff+rod,0),height)
                new=abs(diff-rod);dp[new]=max(dp.get(new,0),height+min(diff,rod))
        return dp[0]
