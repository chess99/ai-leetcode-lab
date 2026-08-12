# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:38Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List

class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        velorunapi = words
        counts = Counter(word[:k] for word in velorunapi if len(word) >= k)
        return sum(count >= 2 for count in counts.values())
