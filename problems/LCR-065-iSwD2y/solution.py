# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        necessary = set(words)
        for word in list(necessary):
            for start in range(1, len(word)):
                necessary.discard(word[start:])
        return sum(len(word) + 1 for word in necessary)
