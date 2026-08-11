# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumGame(self, num: str) -> bool:
        half = len(num) // 2
        left = sum(int(char) for char in num[:half] if char != '?')
        right = sum(int(char) for char in num[half:] if char != '?')
        questions = num[:half].count('?') - num[half:].count('?')
        return questions % 2 != 0 or left - right != -questions // 2 * 9
