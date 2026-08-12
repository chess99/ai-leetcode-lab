# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        candidates = words[:]
        for _ in range(30):
            if not candidates:
                return
            guess = min(candidates, key=lambda word: max(
                (sum(sum(a == b for a, b in zip(word, other)) == score
                     for other in candidates) for score in range(7)), default=0))
            matched = master.guess(guess)
            if matched == 6:
                return
            candidates = [word for word in candidates
                          if sum(a == b for a, b in zip(word, guess)) == matched]
