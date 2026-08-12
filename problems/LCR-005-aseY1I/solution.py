# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = []
        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            masks.append((mask, len(word)))
        answer = 0
        for i in range(len(words)):
            for j in range(i):
                if masks[i][0] & masks[j][0] == 0:
                    answer = max(answer, masks[i][1] * masks[j][1])
        return answer
