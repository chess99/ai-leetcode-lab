# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:39:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(index//8+1 for index in range(len(word)))
