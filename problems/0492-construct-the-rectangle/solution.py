# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:37:22Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = int(area ** 0.5)
        while area % width:
            width -= 1
        return [area // width, width]
