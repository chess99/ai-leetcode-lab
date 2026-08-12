# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dictionary = set()
        answer = []
        for word in sorted(words, key=len):
            reachable = [False] * (len(word) + 1)
            reachable[0] = True
            for end in range(1, len(word) + 1):
                reachable[end] = any(reachable[start] and word[start:end] in dictionary
                                     for start in range(end))
            if reachable[-1]:
                answer.append(word)
            dictionary.add(word)
        return answer
