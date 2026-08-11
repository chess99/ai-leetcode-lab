# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:30:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = [0]
        for word in arr:
            mask = 0
            for character in word:
                bit = 1 << (ord(character) - ord('a'))
                if mask & bit:
                    mask = 0
                    break
                mask |= bit
            if mask:
                masks += [existing | mask for existing in masks if not existing & mask]
        return max(mask.bit_count() for mask in masks)
