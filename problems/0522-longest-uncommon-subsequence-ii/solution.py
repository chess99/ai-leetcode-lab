# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:13:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(shorter: str, longer: str) -> bool:
            position = 0
            for char in longer:
                if position < len(shorter) and shorter[position] == char:
                    position += 1
            return position == len(shorter)

        for index, candidate in sorted(
            enumerate(strs), key=lambda item: len(item[1]), reverse=True
        ):
            if all(
                index == other_index or not is_subsequence(candidate, other)
                for other_index, other in enumerate(strs)
            ):
                return len(candidate)
        return -1
