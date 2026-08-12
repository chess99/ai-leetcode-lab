# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:55Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def search(start1: int, start2: int, length: int) -> bool:
            first = s1[start1:start1 + length]
            second = s2[start2:start2 + length]
            if first == second:
                return True
            if sorted(first) != sorted(second):
                return False
            for split in range(1, length):
                if (search(start1, start2, split)
                        and search(start1 + split, start2 + split, length - split)):
                    return True
                if (search(start1, start2 + length - split, split)
                        and search(start1 + split, start2, length - split)):
                    return True
            return False

        return search(0, 0, len(s1))
