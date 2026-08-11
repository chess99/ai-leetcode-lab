# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:19:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum,accounts))
