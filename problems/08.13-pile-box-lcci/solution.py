# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        box.sort()
        best = [item[2] for item in box]
        answer = 0
        for bottom in range(len(box)):
            width, depth, height = box[bottom]
            for top in range(bottom):
                if box[top][0] < width and box[top][1] < depth and box[top][2] < height:
                    best[bottom] = max(best[bottom], best[top] + height)
            answer = max(answer, best[bottom])
        return answer
