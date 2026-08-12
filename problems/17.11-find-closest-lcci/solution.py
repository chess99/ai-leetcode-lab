# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:22:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        last1 = last2 = -1
        answer = len(words)
        for index, word in enumerate(words):
            if word == word1:
                last1 = index
                if last2 >= 0:
                    answer = min(answer, last1 - last2)
            elif word == word2:
                last2 = index
                if last1 >= 0:
                    answer = min(answer, last2 - last1)
        return answer
