# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:39:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        return sum(words[j].startswith(words[i]) and words[j].endswith(words[i]) for i in range(len(words)) for j in range(i+1,len(words)))
