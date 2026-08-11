# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:52:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit: stack.pop(); k -= 1
            stack.append(digit)
        result = "".join(stack[:-k] if k else stack).lstrip("0")
        return result or "0"
