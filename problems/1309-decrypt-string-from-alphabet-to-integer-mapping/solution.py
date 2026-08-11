# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:46:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#': value, i = int(s[i-2:i]), i - 3
            else: value, i = int(s[i]), i - 1
            result.append(chr(96 + value))
        return ''.join(reversed(result))
