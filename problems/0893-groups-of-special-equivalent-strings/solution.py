# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:56:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        return len({("".join(sorted(word[::2])), "".join(sorted(word[1::2]))) for word in words})
