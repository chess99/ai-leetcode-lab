# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:08:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s=str(num);maximum=int(s.replace(next((c for c in s if c!='9'),'9'),'9'));minimum=int(s.replace(s[0],'0'));return maximum-minimum
