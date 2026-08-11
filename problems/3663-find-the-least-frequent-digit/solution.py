# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:08:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        frequency = {}
        for digit in str(n):
            frequency[digit] = frequency.get(digit, 0) + 1
        return int(min(frequency, key=lambda digit: (frequency[digit], int(digit))))
