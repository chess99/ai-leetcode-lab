# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:19:32Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pieces = {piece[0]: piece for piece in pieces}
        i = 0
        while i < len(arr):
            piece = pieces.get(arr[i])
            if not piece or arr[i:i+len(piece)] != piece: return False
            i += len(piece)
        return True
