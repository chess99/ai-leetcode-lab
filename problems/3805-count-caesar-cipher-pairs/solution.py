# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:34Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List

class Solution:
    def countPairs(self, words: List[str]) -> int:
        bravintelo = words
        count = Counter()
        answer = 0
        for word in bravintelo:
            base = ord(word[0])
            signature = tuple((ord(char) - base) % 26 for char in word)
            answer += count[signature]
            count[signature] += 1
        return answer
