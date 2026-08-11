# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:14Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sortVowels(self, s: str) -> str:
        v=set('aeiouAEIOU'); chars=sorted(x for x in s if x in v); it=iter(chars)
        return ''.join(next(it) if x in v else x for x in s)
