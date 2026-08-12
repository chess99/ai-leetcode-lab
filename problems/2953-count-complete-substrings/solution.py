# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        def count_segment(segment):
            answer = 0
            size = len(segment)
            for distinct in range(1, 27):
                length = distinct * k
                if length > size:
                    break
                frequencies = [0] * 26
                exact = 0
                for index, character in enumerate(segment):
                    value = ord(character) - 97
                    if frequencies[value] == k:
                        exact -= 1
                    frequencies[value] += 1
                    if frequencies[value] == k:
                        exact += 1
                    if index >= length:
                        removed = ord(segment[index - length]) - 97
                        if frequencies[removed] == k:
                            exact -= 1
                        frequencies[removed] -= 1
                        if frequencies[removed] == k:
                            exact += 1
                    if index + 1 >= length and exact == distinct:
                        answer += 1
            return answer

        answer = 0
        start = 0
        for index in range(1, len(word)):
            if abs(ord(word[index]) - ord(word[index - 1])) > 2:
                answer += count_segment(word[start:index])
                start = index
        return answer + count_segment(word[start:])
