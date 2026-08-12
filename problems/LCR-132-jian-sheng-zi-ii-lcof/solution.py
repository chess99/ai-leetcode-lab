# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:32Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def cuttingBamboo(self, bamboo_len: int) -> int:
        if bamboo_len <= 3: return bamboo_len - 1
        count, rest = divmod(bamboo_len, 3)
        if rest == 1: count, rest = count - 1, 4
        elif rest == 2: rest = 2
        else: rest = 1
        return pow(3, count, 1_000_000_007) * rest % 1_000_000_007
