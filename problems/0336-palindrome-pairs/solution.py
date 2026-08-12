# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        indices = {word: index for index, word in enumerate(words)}
        answer = []
        for index, word in enumerate(words):
            for split in range(len(word) + 1):
                left, right = word[:split], word[split:]
                if left == left[::-1]:
                    other = indices.get(right[::-1])
                    if other is not None and other != index:
                        answer.append([other, index])
                if split < len(word) and right == right[::-1]:
                    other = indices.get(left[::-1])
                    if other is not None and other != index:
                        answer.append([index, other])
        return answer
