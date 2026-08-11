# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:27:35Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        return [words[index + 2] for index in range(len(words) - 2)
                if words[index] == first and words[index + 1] == second]
