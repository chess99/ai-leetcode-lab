# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:42Z
# Experiment: ai-leetcode-lab, round 1
from functools import cmp_to_key
from typing import List


class Solution:
    def crackPassword(self, password: List[int]) -> str:
        words = list(map(str, password))

        def compare(left: str, right: str) -> int:
            if left + right < right + left:
                return -1
            if left + right > right + left:
                return 1
            return 0

        words.sort(key=cmp_to_key(compare))
        return ''.join(words)
