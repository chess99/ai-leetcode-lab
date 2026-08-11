# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:53Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        counts = Counter()
        for daily in responses:
            counts.update(set(daily))
        return min(counts, key=lambda word: (-counts[word], word))
