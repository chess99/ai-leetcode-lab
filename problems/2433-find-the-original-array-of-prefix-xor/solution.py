# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        original = [pref[0]]

        for index in range(1, len(pref)):
            original.append(pref[index - 1] ^ pref[index])

        return original
