# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:19:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countCommas(self, n: int) -> int:
        # n 不超过 100000，因此只有四位及以上的数各含一个逗号。
        return max(0, n - 999)
