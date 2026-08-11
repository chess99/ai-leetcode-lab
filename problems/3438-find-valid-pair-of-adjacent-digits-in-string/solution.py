# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:00:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findValidPair(self, s: str) -> str:
        frequency = {}
        for digit in s:
            frequency[digit] = frequency.get(digit, 0) + 1
        for first, second in zip(s, s[1:]):
            if first != second and frequency[first] == int(first) and frequency[second] == int(second):
                return first + second
        return ""
