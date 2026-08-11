# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:57:04Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reformat(self, s: str) -> str:
        letters = [ch for ch in s if ch.isalpha()]
        digits = [ch for ch in s if ch.isdigit()]
        if abs(len(letters) - len(digits)) > 1: return ''
        if len(digits) > len(letters): letters, digits = digits, letters
        return ''.join(a + b for a, b in zip(letters, digits)) + (letters[-1] if len(letters) > len(digits) else '')
