# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:25Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        loads = [0] * k
        best = sum(cookies)

        def search(index: int) -> None:
            nonlocal best
            if index == len(cookies):
                best = min(best, max(loads))
                return

            seen_loads = set()
            for child in range(k):
                if loads[child] in seen_loads:
                    continue
                seen_loads.add(loads[child])
                loads[child] += cookies[index]
                if loads[child] < best:
                    search(index + 1)
                loads[child] -= cookies[index]

        search(0)
        return best
