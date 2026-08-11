# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:22Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        covered = 0
        answer = 0
        right = 0

        for left, (start, _) in enumerate(tiles):
            carpet_end = start + carpetLen - 1
            while right < len(tiles) and tiles[right][1] <= carpet_end:
                covered += tiles[right][1] - tiles[right][0] + 1
                right += 1

            partial = 0
            if right < len(tiles):
                partial = max(0, min(carpet_end, tiles[right][1]) - tiles[right][0] + 1)
            answer = max(answer, covered + partial)

            if left < right:
                covered -= tiles[left][1] - tiles[left][0] + 1
            else:
                right = left + 1

        return answer
