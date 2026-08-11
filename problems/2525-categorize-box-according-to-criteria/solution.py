# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:05:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = max(length, width, height) >= 10000 or length * width * height >= 10**9
        heavy = mass >= 100
        return 'Both' if bulky and heavy else ('Bulky' if bulky else ('Heavy' if heavy else 'Neither'))
