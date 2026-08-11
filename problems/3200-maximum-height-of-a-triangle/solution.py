# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:47:35Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def height(first: int, second: int) -> int:
            level = 1
            while True:
                if level % 2 == 1:
                    if first < level:
                        return level - 1
                    first -= level
                else:
                    if second < level:
                        return level - 1
                    second -= level
                level += 1

        return max(height(red, blue), height(blue, red))
