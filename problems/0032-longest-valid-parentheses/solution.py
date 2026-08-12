# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        answer = 0
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            else:
                stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    answer = max(answer, index - stack[-1])
        return answer
