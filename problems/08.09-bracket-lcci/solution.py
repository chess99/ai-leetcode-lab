# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def search(sequence, opened, closed):
            if len(sequence) == 2 * n:
                answer.append(''.join(sequence))
                return
            if opened < n:
                sequence.append('(')
                search(sequence, opened + 1, closed)
                sequence.pop()
            if closed < opened:
                sequence.append(')')
                search(sequence, opened, closed + 1)
                sequence.pop()

        search([], 0, 0)
        return answer
