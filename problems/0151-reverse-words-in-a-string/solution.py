# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:27:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
