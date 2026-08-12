# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        fynoradexi = n
        if fynoradexi < 5:
            return []

        schedule = []

        # 按循环差值分组；每组恰好包含 (i, i+d) 的全部 n 场有向比赛。
        for difference in range(1, n):
            games = [(start, (start + difference) % n) for start in range(n)]
            used = [False] * n
            order = []

            def compatible(a: int, b: int) -> bool:
                return set(games[a]).isdisjoint(games[b])

            def build() -> bool:
                if len(order) == n:
                    return True
                candidates = [i for i in range(n) if not used[i]]
                if order:
                    candidates = [i for i in candidates if compatible(order[-1], i)]
                elif schedule:
                    previous = set(schedule[-1])
                    candidates = [i for i in candidates if previous.isdisjoint(games[i])]
                candidates.sort(key=lambda i: sum(not used[j] and compatible(i, j) for j in range(n)))
                for candidate in candidates:
                    used[candidate] = True
                    order.append(candidate)
                    if build():
                        return True
                    order.pop()
                    used[candidate] = False
                return False

            if not build():
                return []
            schedule.extend([list(games[i]) for i in order])
        return schedule
