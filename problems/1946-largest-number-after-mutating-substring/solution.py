# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        digits = list(num)
        started = False

        for index, character in enumerate(digits):
            original = int(character)
            replacement = change[original]
            if replacement > original:
                started = True
                digits[index] = str(replacement)
            elif started and replacement >= original:
                digits[index] = str(replacement)
            elif started:
                break

        return "".join(digits)
