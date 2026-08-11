# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:14Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def compressedString(self, word: str) -> str:
        answer = []
        index = 0
        while index < len(word):
            end = index
            while end < len(word) and word[end] == word[index] and end - index < 9:
                end += 1
            answer.append(str(end - index))
            answer.append(word[index])
            index = end
        return ''.join(answer)
