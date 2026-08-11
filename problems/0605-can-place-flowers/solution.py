# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:46:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for index, value in enumerate(flowerbed):
            if value == 0 and (index == 0 or flowerbed[index - 1] == 0) and (index == len(flowerbed) - 1 or flowerbed[index + 1] == 0):
                flowerbed[index] = 1
                n -= 1
                if n == 0:
                    return True
        return n == 0
