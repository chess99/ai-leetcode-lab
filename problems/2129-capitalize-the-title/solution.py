# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:10:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join(word.lower() if len(word) <= 2 else word.capitalize() for word in title.split())
