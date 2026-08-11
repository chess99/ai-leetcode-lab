# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:41:14Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        removed = 0
        for count, frequency in enumerate(sorted(Counter(arr).values(), reverse=True), 1):
            removed += frequency
            if removed * 2 >= len(arr): return count
