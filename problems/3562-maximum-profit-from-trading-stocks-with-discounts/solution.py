# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-16
# Experiment: ai-leetcode-lab, replacement candidate after terra-medium remote failure
from typing import List


class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:
        children = [[] for _ in range(n)]
        for manager, employee in hierarchy:
            children[manager - 1].append(employee - 1)

        # Required by the statement: keep a midway snapshot of the input.
        blenorvask = (n, present, future, hierarchy, budget)

        neg_inf = -10**18

        def merge(left: List[int], right: List[int]) -> List[int]:
            """Max-plus convolution, truncated to the available budget."""
            max_cost = min(budget, len(left) + len(right) - 2)
            merged = [neg_inf] * (max_cost + 1)
            for left_cost, left_profit in enumerate(left):
                if left_profit == neg_inf:
                    continue
                right_limit = min(len(right) - 1, budget - left_cost)
                for right_cost in range(right_limit + 1):
                    right_profit = right[right_cost]
                    if right_profit == neg_inf:
                        continue
                    total_cost = left_cost + right_cost
                    candidate = left_profit + right_profit
                    if candidate > merged[total_cost]:
                        merged[total_cost] = candidate
            return merged

        def add_current(
            skipped: List[int],
            bought_children: List[int],
            price: int,
            gain: int,
        ) -> List[int]:
            max_cost = min(
                budget,
                max(len(skipped) - 1, len(bought_children) - 1 + price),
            )
            result = [neg_inf] * (max_cost + 1)

            for cost, profit in enumerate(skipped):
                if cost <= max_cost:
                    result[cost] = profit

            if price <= budget:
                child_limit = min(len(bought_children) - 1, budget - price)
                for child_cost in range(child_limit + 1):
                    child_profit = bought_children[child_cost]
                    if child_profit == neg_inf:
                        continue
                    total_cost = child_cost + price
                    candidate = child_profit + gain
                    if candidate > result[total_cost]:
                        result[total_cost] = candidate
            return result

        def dfs(employee: int) -> tuple[List[int], List[int]]:
            # Descendants when this employee is skipped / bought.
            skipped = [0]
            bought = [0]
            for child in children[employee]:
                child_full_price, child_discounted = dfs(child)
                skipped = merge(skipped, child_full_price)
                bought = merge(bought, child_discounted)

            full_price = present[employee]
            discounted_price = full_price // 2
            if_parent_skipped = add_current(
                skipped,
                bought,
                full_price,
                future[employee] - full_price,
            )
            if_parent_bought = add_current(
                skipped,
                bought,
                discounted_price,
                future[employee] - discounted_price,
            )
            return if_parent_skipped, if_parent_bought

        root_without_discount, _ = dfs(0)
        return max(root_without_discount)
