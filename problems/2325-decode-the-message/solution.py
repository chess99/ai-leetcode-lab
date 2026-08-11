# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:20:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping={}; index=0
        for char in key:
            if char!=' ' and char not in mapping:mapping[char]=chr(97+index);index+=1
        return ''.join(mapping.get(char,' ') for char in message)
