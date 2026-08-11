# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:05:55Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(char*count for char,count in Counter(s).most_common())
