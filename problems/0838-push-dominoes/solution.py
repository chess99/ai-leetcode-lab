# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:48:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        state = list("L" + dominoes + "R")
        previous = 0
        for current in range(1, len(state)):
            if state[current] == ".":
                continue
            if state[previous] == state[current]:
                for index in range(previous + 1, current):
                    state[index] = state[current]
            elif state[previous] == "R" and state[current] == "L":
                left, right = previous + 1, current - 1
                while left < right:
                    state[left] = "R"
                    state[right] = "L"
                    left += 1
                    right -= 1
            previous = current
        return "".join(state[1:-1])
