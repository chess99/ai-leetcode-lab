# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        answer = []

        def dfs(prefix: str) -> None:
            if len(prefix) == n:
                answer.append(prefix)
                return
            if not prefix or prefix[-1] == '1':
                dfs(prefix + '0')
            dfs(prefix + '1')

        dfs('')
        return answer
