# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:09Z
# Experiment: ai-leetcode-lab, round 1


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        answer = []
        pending = []
        for index in range(len(pattern) + 1):
            pending.append(str(index + 1))
            if index == len(pattern) or pattern[index] == "I":
                while pending:
                    answer.append(pending.pop())
        return "".join(answer)
