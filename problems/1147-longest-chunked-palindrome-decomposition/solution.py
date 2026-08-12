# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestDecomposition(self, text: str) -> int:
        left_piece = ''
        right_piece = ''
        answer = 0
        size = len(text)
        for index, char in enumerate(text):
            left_piece += char
            right_piece = text[size - 1 - index] + right_piece
            if left_piece == right_piece:
                answer += 1
                left_piece = right_piece = ''
        return answer
