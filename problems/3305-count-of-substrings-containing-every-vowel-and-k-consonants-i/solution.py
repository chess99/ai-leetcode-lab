# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")
        def at_most(limit: int) -> int:
            if limit < 0:
                return 0
            left = consonants = total = 0
            last = {v: -1 for v in vowels}
            for right, char in enumerate(word):
                if char in vowels:
                    last[char] = right
                else:
                    consonants += 1
                while consonants > limit:
                    if word[left] not in vowels:
                        consonants -= 1
                    left += 1
                first_complete = min(last.values())
                if first_complete >= left:
                    total += first_complete - left + 1
            return total
        return at_most(k) - at_most(k - 1)
