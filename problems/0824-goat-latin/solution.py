# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:05:24Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = []
        vowels = set("aeiouAEIOU")
        for index, word in enumerate(sentence.split(), 1):
            if word[0] not in vowels:
                word = word[1:] + word[0]
            words.append(word + "ma" + "a" * index)
        return " ".join(words)
