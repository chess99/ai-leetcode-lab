# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:41:16Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(s) - Counter(t)).values())
