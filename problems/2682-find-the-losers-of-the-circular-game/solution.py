# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:12:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        visited = [False] * n
        position = 0
        turn = 1

        while not visited[position]:
            visited[position] = True
            position = (position + turn * k) % n
            turn += 1

        return [player + 1 for player, seen in enumerate(visited) if not seen]
