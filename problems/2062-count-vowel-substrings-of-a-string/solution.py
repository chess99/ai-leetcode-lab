# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:03:22Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels=set('aeiou');total=0
        for i in range(len(word)):
            found=set()
            for j in range(i,len(word)):
                if word[j] not in vowels:break
                found.add(word[j]);total+=len(found)==5
        return total
