# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:37:13Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        answer = []
        prefix = ''
        start = 0
        for character in searchWord:
            prefix += character
            start = bisect_left(products, prefix, start)
            answer.append([product for product in products[start:start + 3] if product.startswith(prefix)])
        return answer
