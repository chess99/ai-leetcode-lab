# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:48:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        for index, source, target in sorted(zip(indices, sources, targets), reverse=True):
            if s.startswith(source, index):
                s = s[:index] + target + s[index + len(source):]
        return s
