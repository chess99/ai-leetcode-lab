# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:21:12Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        remaining = Counter(s)
        stack = []
        in_stack = set()

        for ch in s:
            remaining[ch] -= 1
            if ch in in_stack:
                continue
            while stack and ch < stack[-1] and remaining[stack[-1]] > 0:
                in_stack.remove(stack.pop())
            stack.append(ch)
            in_stack.add(ch)
        return "".join(stack)
