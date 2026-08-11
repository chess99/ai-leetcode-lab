# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:46:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1; total=0
        while n:
            n,digit=divmod(n,10); product*=digit; total+=digit
        return product-total
