# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:06:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words=text.split(); spaces=text.count(' ')
        if len(words)==1:return words[0]+' '*spaces
        gap,extra=divmod(spaces,len(words)-1); return (' '*gap).join(words)+' '*extra
