# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
        columns = len(frame[0])
        dp = [0] * columns
        for row in frame:
            for column, value in enumerate(row):
                left = dp[column - 1] if column else 0
                dp[column] = max(dp[column], left) + value
        return dp[-1]
