# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def cuttingBamboo(self, bamboo_len: int) -> int:
        if bamboo_len <= 3: return bamboo_len - 1
        count, rest = divmod(bamboo_len, 3)
        if rest == 0: return 3 ** count
        if rest == 1: return 3 ** (count - 1) * 4
        return 3 ** count * 2
