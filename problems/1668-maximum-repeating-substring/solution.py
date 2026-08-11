# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:20:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        while word * (count + 1) in sequence: count += 1
        return count
