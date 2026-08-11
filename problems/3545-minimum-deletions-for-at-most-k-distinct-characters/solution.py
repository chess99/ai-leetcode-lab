# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:04:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        return sum(sorted(counts.values())[:max(0, len(counts) - k)])
