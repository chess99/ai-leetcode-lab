# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:58:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            if op == '+':
                scores.append(scores[-1] + scores[-2])
            elif op == 'D':
                scores.append(2 * scores[-1])
            elif op == 'C':
                scores.pop()
            else:
                scores.append(int(op))
        return sum(scores)
