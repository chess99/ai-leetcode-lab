# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:49:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minNumberOfFrogs(self, croak_of_frogs: str) -> int:
        stage = {character: index for index, character in enumerate("croak")}
        counts = [0] * 5
        maximum = 0
        for character in croak_of_frogs:
            index = stage[character]
            if index == 0:
                counts[0] += 1
            elif counts[index - 1] == 0:
                return -1
            else:
                counts[index - 1] -= 1
                counts[index] += 1
            if index == 4:
                counts[4] -= 1
            maximum = max(maximum, sum(counts))
        return maximum if not any(counts) else -1
