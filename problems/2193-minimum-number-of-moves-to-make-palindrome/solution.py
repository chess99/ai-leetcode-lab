# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        characters = list(s)
        left = 0
        right = len(characters) - 1
        answer = 0
        while left < right:
            if characters[left] == characters[right]:
                left += 1
                right -= 1
                continue

            match = right
            while match > left and characters[match] != characters[left]:
                match -= 1
            if match == left:
                characters[left], characters[left + 1] = (
                    characters[left + 1], characters[left]
                )
                answer += 1
            else:
                while match < right:
                    characters[match], characters[match + 1] = (
                        characters[match + 1], characters[match]
                    )
                    match += 1
                    answer += 1
                left += 1
                right -= 1
        return answer
