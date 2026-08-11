# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:57:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image
        stack = [(sr, sc)]
        while stack:
            row, col = stack.pop()
            if not (0 <= row < len(image) and 0 <= col < len(image[0])) or image[row][col] != original:
                continue
            image[row][col] = color
            stack.extend(((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)))
        return image
