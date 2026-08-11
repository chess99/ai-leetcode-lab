# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:32:58Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join(word[:-1] for word in sorted(s.split(),key=lambda word:word[-1]))
