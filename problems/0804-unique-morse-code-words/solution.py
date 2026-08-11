# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:04:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes=['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
        return len({''.join(codes[ord(char)-97] for char in word) for word in words})
