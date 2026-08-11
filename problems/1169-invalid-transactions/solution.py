# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:26:23Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []
        invalid = set()
        for index, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            parsed.append((name, int(time), int(amount), city))
            if int(amount) > 1000:
                invalid.add(index)

        for i, (name, time, _, city) in enumerate(parsed):
            for j in range(i + 1, len(parsed)):
                other_name, other_time, _, other_city = parsed[j]
                if name == other_name and city != other_city and abs(time - other_time) <= 60:
                    invalid.add(i)
                    invalid.add(j)

        return [transaction for index, transaction in enumerate(transactions) if index in invalid]
