# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:56:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        combined = ''
        for word in words:
            combined += word
            if combined == s:
                return True
            if len(combined) >= len(s):
                return False
        return False
