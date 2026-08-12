# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        path = []

        def backtrack(opened: int, closed: int) -> None:
            if closed == n:
                answer.append(''.join(path))
                return
            if opened < n:
                path.append('(')
                backtrack(opened + 1, closed)
                path.pop()
            if closed < opened:
                path.append(')')
                backtrack(opened, closed + 1)
                path.pop()

        backtrack(0, 0)
        return answer
