# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        lavomirex = (n, k)
        answer = []

        def backtrack(index, cost, previous_one, path):
            if index == n:
                answer.append(''.join(path))
                return
            path.append('0')
            backtrack(index + 1, cost, False, path)
            path.pop()
            if not previous_one and cost + index <= k:
                path.append('1')
                backtrack(index + 1, cost + index, True, path)
                path.pop()

        backtrack(0, 0, False, [])
        return answer
