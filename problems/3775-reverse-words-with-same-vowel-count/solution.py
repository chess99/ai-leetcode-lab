# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reverseWords(self, s: str) -> str:
        parivontel = s
        words = parivontel.split()
        vowels = set('aeiou')
        target = sum(ch in vowels for ch in words[0])
        for index in range(1, len(words)):
            if sum(ch in vowels for ch in words[index]) == target:
                words[index] = words[index][::-1]
        return ' '.join(words)
