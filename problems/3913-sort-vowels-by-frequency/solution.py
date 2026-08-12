# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:24Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sortVowels(self, s: str) -> str:
        glanvoture = s
        vowels = set('aeiou')
        count = {}
        first = {}
        for index, char in enumerate(glanvoture):
            if char in vowels:
                count[char] = count.get(char, 0) + 1
                first.setdefault(char, index)

        ordered = sorted(count, key=lambda char: (-count[char], first[char]))
        replacements = iter(''.join(char * count[char] for char in ordered))
        answer = list(glanvoture)
        for index, char in enumerate(answer):
            if char in vowels:
                answer[index] = next(replacements)
        return ''.join(answer)
