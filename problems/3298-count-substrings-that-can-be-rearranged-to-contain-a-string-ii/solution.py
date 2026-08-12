# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        need = [0] * 26
        for character in word2:
            need[ord(character) - 97] += 1
        missing = len(word2)
        counts = [0] * 26
        left = 0
        answer = 0
        for right, character in enumerate(word1):
            index = ord(character) - 97
            counts[index] += 1
            if counts[index] <= need[index]:
                missing -= 1
            while missing == 0:
                removed = ord(word1[left]) - 97
                counts[removed] -= 1
                left += 1
                if counts[removed] < need[removed]:
                    missing += 1
            answer += left
        return answer
