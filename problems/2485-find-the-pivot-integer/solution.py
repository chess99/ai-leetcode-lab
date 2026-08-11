# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:03:44Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def pivotInteger(self, n: int) -> int:
        total=n*(n+1)//2; root=int(total**0.5);return root if root*root==total else -1
