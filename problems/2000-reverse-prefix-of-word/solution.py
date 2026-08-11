# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:52:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index=word.find(ch)
        return word if index < 0 else word[:index+1][::-1]+word[index+1:]
