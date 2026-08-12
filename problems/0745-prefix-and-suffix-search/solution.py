# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.indices = {}
        for index, word in enumerate(words):
            for prefix_length in range(len(word) + 1):
                for suffix_length in range(len(word) + 1):
                    self.indices[word[:prefix_length],
                                 word[len(word) - suffix_length:]] = index

    def f(self, pref: str, suff: str) -> int:
        return self.indices.get((pref, suff), -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
