# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:25:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return ''.join(word[0] for word in words) == s
