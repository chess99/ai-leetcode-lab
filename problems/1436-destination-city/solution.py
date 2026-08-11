# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:59:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = {start for start, _ in paths}
        return next(end for _, end in paths if end not in starts)
