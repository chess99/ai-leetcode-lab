# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:03:27Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def oddString(self, words: List[str]) -> str:
        diffs = [tuple(ord(b)-ord(a) for a, b in zip(word, word[1:])) for word in words]
        return words[0] if diffs[0] != diffs[1] and diffs[0] != diffs[2] else (words[1] if diffs[1] != diffs[2] else words[2])
