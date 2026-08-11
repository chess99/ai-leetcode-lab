# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:41:42Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        choices = defaultdict(list)
        for left, right, top in allowed:
            choices[left + right].append(top)

        @lru_cache(maxsize=None)
        def can_build(row: str) -> bool:
            if len(row) == 1:
                return True

            def build(index: int, next_row: str) -> bool:
                if index == len(row) - 1:
                    return can_build(next_row)
                for top in choices[row[index:index + 2]]:
                    if build(index + 1, next_row + top):
                        return True
                return False

            return build(0, "")

        return can_build(bottom)
