# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        pairs = sum(count // 2 for count in Counter(''.join(words)).values())
        answer = 0
        for length in sorted(map(len, words)):
            needed = length // 2
            if pairs < needed:
                break
            pairs -= needed
            answer += 1
        return answer
