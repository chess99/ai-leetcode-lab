# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:26Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        used=set();answer=0
        for frequency in sorted(Counter(s).values(),reverse=True):
            while frequency and frequency in used:frequency-=1;answer+=1
            used.add(frequency)
        return answer
