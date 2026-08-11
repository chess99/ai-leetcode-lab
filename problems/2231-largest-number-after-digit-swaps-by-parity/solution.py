# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:18:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def largestInteger(self, num: int) -> int:
        odds=sorted((char for char in str(num) if int(char)%2),reverse=True); evens=sorted((char for char in str(num) if int(char)%2==0),reverse=True)
        return int(''.join(odds.pop(0) if int(char)%2 else evens.pop(0) for char in str(num)))
