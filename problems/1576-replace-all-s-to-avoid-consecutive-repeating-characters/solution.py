# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:09:43Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def modifyString(self, s: str) -> str:
        chars = list(s)
        for i, ch in enumerate(chars):
            if ch == '?':
                for candidate in 'abc':
                    if (i == 0 or chars[i-1] != candidate) and (i == len(chars)-1 or chars[i+1] != candidate):
                        chars[i] = candidate; break
        return ''.join(chars)
