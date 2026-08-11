# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:26:22Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        counts = Counter(text)
        answer = 0
        for character, total_count in counts.items():
            left = mismatches = 0
            for right, value in enumerate(text):
                if value != character:
                    mismatches += 1
                while mismatches > 1:
                    if text[left] != character:
                        mismatches -= 1
                    left += 1
                answer = max(answer, min(right - left + 1, total_count))
        return answer
