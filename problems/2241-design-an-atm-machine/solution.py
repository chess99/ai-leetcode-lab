# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class ATM:

    def __init__(self):
        self.denominations = [20, 50, 100, 200, 500]
        self.banknotes = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for index, count in enumerate(banknotesCount):
            self.banknotes[index] += count

    def withdraw(self, amount: int) -> List[int]:
        used = [0] * 5
        remaining = amount

        for index in range(4, -1, -1):
            count = min(
                self.banknotes[index],
                remaining // self.denominations[index],
            )
            used[index] = count
            remaining -= count * self.denominations[index]

        if remaining != 0:
            return [-1]

        for index in range(5):
            self.banknotes[index] -= used[index]

        return used


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
