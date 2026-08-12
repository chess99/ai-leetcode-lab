# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def parse(index):
            products = {""}; choices = set()
            while index < len(expression) and expression[index] != '}':
                if expression[index] == ',': choices |= products; products = {""}; index += 1
                elif expression[index] == '{':
                    nested, index = parse(index + 1); products = {a + b for a in products for b in nested}; index += 1
                else:
                    products = {a + expression[index] for a in products}; index += 1
            return choices | products, index
        return sorted(parse(0)[0])
