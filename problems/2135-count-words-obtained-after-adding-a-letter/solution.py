# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:27Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def mask(word: str) -> int:
            result = 0
            for char in word:
                result |= 1 << (ord(char) - ord("a"))
            return result

        start_masks = {mask(word) for word in startWords}
        answer = 0
        for word in targetWords:
            target_mask = mask(word)
            for char in word:
                previous_mask = target_mask ^ (1 << (ord(char) - ord("a")))
                if previous_mask in start_masks:
                    answer += 1
                    break
        return answer
