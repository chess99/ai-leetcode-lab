# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:06:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = list(range(26))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for equation in equations:
            if equation[1] == "=":
                left = ord(equation[0]) - ord("a")
                right = ord(equation[3]) - ord("a")
                parent[find(left)] = find(right)

        return all(
            equation[1] == "="
            or find(ord(equation[0]) - ord("a")) != find(ord(equation[3]) - ord("a"))
            for equation in equations
        )
