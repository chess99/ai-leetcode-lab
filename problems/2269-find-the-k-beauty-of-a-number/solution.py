# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:46:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        text = str(num)
        return sum(value != 0 and num % value == 0 for value in (int(text[i:i+k]) for i in range(len(text)-k+1)))
