# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minimumLength(self, s: str) -> int:
        from collections import Counter
        return sum(1 if count % 2 else 2 for count in Counter(s).values())
