# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:42:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        counts = Counter(arr).values()
        return len(counts) == len(set(counts))
