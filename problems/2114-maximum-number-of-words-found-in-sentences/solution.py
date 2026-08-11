# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:09:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(sentence.count(' ') + 1 for sentence in sentences)
