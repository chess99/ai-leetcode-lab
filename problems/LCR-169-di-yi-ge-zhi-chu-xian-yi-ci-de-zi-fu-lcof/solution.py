# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:45:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def dismantlingAction(self, arr: str) -> str:
        counts = {}
        for char in arr:
            counts[char] = counts.get(char, 0) + 1
        return next((char for char in arr if counts[char] == 1), ' ')
