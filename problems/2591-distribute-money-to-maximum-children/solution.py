# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:07:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        eight_count = min(money // 7, children)
        money -= eight_count * 7
        children -= eight_count
        if children == 0 and money > 0:
            return eight_count - 1
        if children == 1 and money == 3:
            return eight_count - 1
        return eight_count
