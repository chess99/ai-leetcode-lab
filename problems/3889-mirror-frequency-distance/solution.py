# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:43Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def mirrorFrequency(self, s: str) -> int:
        counts = Counter(s)
        answer = 0
        for index in range(13):
            answer += abs(counts[chr(ord('a') + index)] - counts[chr(ord('z') - index)])
        for index in range(5):
            answer += abs(counts[str(index)] - counts[str(9 - index)])
        return answer
