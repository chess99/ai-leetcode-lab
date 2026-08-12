# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:45Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def appealSum(self, s: str) -> int:
        last = {}
        ending = 0
        answer = 0
        for index, character in enumerate(s):
            ending += index - last.get(character, -1)
            last[character] = index
            answer += ending
        return answer
