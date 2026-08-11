# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:30Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_orders = []
        sell_orders = []

        for price, amount, order_type in orders:
            if order_type == 0:
                while amount and sell_orders and sell_orders[0][0] <= price:
                    sell_price, sell_amount = heapq.heappop(sell_orders)
                    matched = min(amount, sell_amount)
                    amount -= matched
                    sell_amount -= matched
                    if sell_amount:
                        heapq.heappush(sell_orders, (sell_price, sell_amount))
                if amount:
                    heapq.heappush(buy_orders, (-price, amount))
            else:
                while amount and buy_orders and -buy_orders[0][0] >= price:
                    buy_price, buy_amount = heapq.heappop(buy_orders)
                    matched = min(amount, buy_amount)
                    amount -= matched
                    buy_amount -= matched
                    if buy_amount:
                        heapq.heappush(buy_orders, (buy_price, buy_amount))
                if amount:
                    heapq.heappush(sell_orders, (price, amount))

        backlog = sum(amount for _, amount in buy_orders) + sum(amount for _, amount in sell_orders)
        return backlog % 1_000_000_007
