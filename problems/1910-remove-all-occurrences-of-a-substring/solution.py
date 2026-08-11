# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:04Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_length = len(part)

        for character in s:
            stack.append(character)
            if len(stack) >= part_length and "".join(stack[-part_length:]) == part:
                del stack[-part_length:]

        return "".join(stack)
