# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:03:27Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        diffs = [tuple(ord(b)-ord(a) for a, b in zip(word, word[1:])) for word in words]
        if diffs[0] == diffs[1]:
            return words[2]
        return words[0] if diffs[0] != diffs[2] else words[1]
