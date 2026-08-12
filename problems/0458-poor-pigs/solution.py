# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest // minutesToDie + 1
        pigs = 0
        distinguishable = 1
        while distinguishable < buckets:
            distinguishable *= states
            pigs += 1
        return pigs
