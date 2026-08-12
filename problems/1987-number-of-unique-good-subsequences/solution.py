# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:03Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        mod = 10**9 + 7
        end0 = end1 = 0
        zero = False
        for c in binary:
            if c == '0':
                end0 = (end0 + end1) % mod
                zero = True
            else:
                end1 = (end0 + end1 + 1) % mod
        return (end0 + end1 + zero) % mod
