# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:39:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        height = max(map(len, words))
        return ["".join(word[index] if index < len(word) else " " for word in words).rstrip()
                for index in range(height)]
