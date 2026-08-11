# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:44:45Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        result = []
        for character in order:
            result.append(character * counts.pop(character, 0))
        result.extend(character * count for character, count in counts.items())
        return "".join(result)
