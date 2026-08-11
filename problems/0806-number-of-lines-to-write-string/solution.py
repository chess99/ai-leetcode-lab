# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:04:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines=1; width=0
        for char in s:
            value=widths[ord(char)-97]
            if width+value>100: lines+=1; width=0
            width+=value
        return [lines,width]
