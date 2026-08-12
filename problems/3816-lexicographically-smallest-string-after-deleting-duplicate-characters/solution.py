# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:55Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        tilvarceno = s
        remaining = Counter(s)
        selected = Counter()
        stack = []
        for char in s:
            remaining[char] -= 1
            while (stack and stack[-1] > char
                   and (selected[stack[-1]] > 1 or remaining[stack[-1]] > 0)):
                selected[stack.pop()] -= 1
            stack.append(char)
            selected[char] += 1
        while stack and selected[stack[-1]] > 1:
            selected[stack.pop()] -= 1
        return ''.join(stack)
