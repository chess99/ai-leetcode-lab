# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:54:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for index,word in enumerate(sentence.split(),1):
            if word.startswith(searchWord):return index
        return -1
