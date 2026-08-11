# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:48:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        remaining=set(words)
        for word in words:
            for i in range(1,len(word)): remaining.discard(word[i:])
        return sum(len(word)+1 for word in remaining)
