# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:50:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def deserialize(self, s: str):
        if s[0] != "[":
            return NestedInteger(int(s))

        stack = []
        number_start = 0
        for index, char in enumerate(s):
            if char == "[":
                item = NestedInteger()
                if stack:
                    stack[-1].add(item)
                stack.append(item)
                number_start = index + 1
            elif char in ",]":
                if index > number_start:
                    stack[-1].add(NestedInteger(int(s[number_start:index])))
                if char == "]":
                    finished = stack.pop()
                    if not stack:
                        return finished
                number_start = index + 1
