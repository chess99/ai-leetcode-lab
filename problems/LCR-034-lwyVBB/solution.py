# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:35:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        position = {char: index for index, char in enumerate(order)}
        for first, second in zip(words, words[1:]):
            for a, b in zip(first, second):
                if a != b:
                    if position[a] > position[b]:
                        return False
                    break
            else:
                if len(first) > len(second):
                    return False
        return True
