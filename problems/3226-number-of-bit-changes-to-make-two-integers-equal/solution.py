# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:47:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if k & ~n:
            return -1
        return (n ^ k).bit_count()
