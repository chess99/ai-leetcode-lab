# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:41:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {character: index for index, character in enumerate(s)}
        result = []
        start = end = 0
        for index, character in enumerate(s):
            end = max(end, last[character])
            if index == end:
                result.append(end - start + 1)
                start = index + 1
        return result
