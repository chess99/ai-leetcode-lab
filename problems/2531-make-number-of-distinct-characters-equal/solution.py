# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:25Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        first, second = Counter(word1), Counter(word2)
        for a in first:
            for b in second:
                if a == b:
                    if len(first) == len(second):
                        return True
                    continue
                distinct_first = len(first) - (first[a] == 1) + (b not in first)
                distinct_second = len(second) - (second[b] == 1) + (a not in second)
                if distinct_first == distinct_second:
                    return True
        return False
