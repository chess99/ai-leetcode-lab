# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:42:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def greatestLetter(self, s: str) -> str:
        letters=set(s)
        for code in range(ord('Z'),ord('A')-1,-1):
            if chr(code) in letters and chr(code+32) in letters: return chr(code)
        return ''
