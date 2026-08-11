# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod=10**9+7;maximum=(1<<p)-1
        return maximum*pow(maximum-1,(1<<(p-1))-1,mod)%mod
