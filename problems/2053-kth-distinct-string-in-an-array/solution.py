# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:03:13Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import Counter
        counts = Counter(arr)
        return next((word for word in arr if counts[word] == 1 and not (k := k - 1)), '')
