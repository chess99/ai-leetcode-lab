# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(text: str, first: str, second: str, score: int) -> tuple[str, int]:
            stack = []
            gained = 0
            for character in text:
                if stack and stack[-1] == first and character == second:
                    stack.pop()
                    gained += score
                else:
                    stack.append(character)
            return "".join(stack), gained

        if x >= y:
            remaining, score = remove_pair(s, "a", "b", x)
            _, extra_score = remove_pair(remaining, "b", "a", y)
        else:
            remaining, score = remove_pair(s, "b", "a", y)
            _, extra_score = remove_pair(remaining, "a", "b", x)

        return score + extra_score
