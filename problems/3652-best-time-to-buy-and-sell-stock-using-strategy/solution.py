# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        original = [price * action for price, action in zip(prices, strategy)]
        base = sum(original)
        original_prefix = [0]
        price_prefix = [0]
        for contribution, price in zip(original, prices):
            original_prefix.append(original_prefix[-1] + contribution)
            price_prefix.append(price_prefix[-1] + price)
        answer = base
        half = k // 2
        for left in range(len(prices) - k + 1):
            middle = left + half
            right = left + k
            old = original_prefix[right] - original_prefix[left]
            new = price_prefix[right] - price_prefix[middle]
            answer = max(answer, base - old + new)
        return answer
