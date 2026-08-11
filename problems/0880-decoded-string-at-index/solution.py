# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:56:14Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size=0
        for char in s:
            size=size*int(char) if char.isdigit() else size+1
        for char in reversed(s):
            k%=size
            if k==0 and char.isalpha(): return char
            size=size//int(char) if char.isdigit() else size-1
