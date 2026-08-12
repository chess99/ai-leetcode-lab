# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:39:01Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        cap = 10**15 + 1
        factorial = [1] * (n + 1)
        for value in range(1, n + 1):
            factorial[value] = min(cap, factorial[value - 1] * value)

        def completions(odds: int, evens: int, next_parity: int) -> int:
            remaining = odds + evens
            needed_odds = (remaining + (next_parity == 1)) // 2
            needed_evens = remaining - needed_odds
            if odds != needed_odds or evens != needed_evens:
                return 0
            return min(cap, factorial[odds] * factorial[evens])

        unused = list(range(1, n + 1))
        odds, evens = (n + 1) // 2, n // 2
        answer = []
        previous_parity = -1
        for _ in range(n):
            chosen = None
            for value in unused:
                parity = value & 1
                if previous_parity == parity:
                    continue
                remaining_odds = odds - parity
                remaining_evens = evens - (1 - parity)
                ways = 1 if not answer and n == 1 else completions(
                    remaining_odds, remaining_evens, 1 - parity
                )
                if k > ways:
                    k -= ways
                else:
                    chosen = value
                    break
            if chosen is None:
                return []
            unused.remove(chosen)
            parity = chosen & 1
            odds -= parity
            evens -= 1 - parity
            previous_parity = parity
            answer.append(chosen)
        return answer
