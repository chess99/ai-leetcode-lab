# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:42:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        total=previous=0
        for upper,percent in brackets:
            taxable=min(income,upper)-previous
            if taxable>0: total+=taxable*percent/100
            previous=upper
            if income<=upper: break
        return total
