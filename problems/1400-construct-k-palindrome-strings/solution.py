# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:49:29Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return k <= len(s) and sum(count % 2 for count in Counter(s).values()) <= k
