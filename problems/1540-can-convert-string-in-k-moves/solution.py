# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:55:40Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t): return False
        shifts = Counter((ord(b) - ord(a)) % 26 for a, b in zip(s, t) if a != b)
        return all(shift + 26 * (count - 1) <= k for shift, count in shifts.items())
