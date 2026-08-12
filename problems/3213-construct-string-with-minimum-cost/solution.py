# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:30Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        children: list[dict[str, int]] = [{}]
        fail = [0]
        output_link = [-1]
        terminal: list[tuple[int, int] | None] = [None]

        for word, cost in zip(words, costs):
            node = 0
            for char in word:
                next_node = children[node].get(char)
                if next_node is None:
                    next_node = len(children)
                    children[node][char] = next_node
                    children.append({})
                    fail.append(0)
                    output_link.append(-1)
                    terminal.append(None)
                node = next_node
            old = terminal[node]
            if old is None or cost < old[1]:
                terminal[node] = (len(word), cost)

        queue = deque()
        for node in children[0].values():
            queue.append(node)

        while queue:
            node = queue.popleft()
            fallback = fail[node]
            output_link[node] = fallback if terminal[fallback] is not None else output_link[fallback]
            for char, next_node in children[node].items():
                fallback = fail[node]
                while fallback and char not in children[fallback]:
                    fallback = fail[fallback]
                fail[next_node] = children[fallback].get(char, 0)
                queue.append(next_node)

        inf = 10**30
        dp = [inf] * (len(target) + 1)
        dp[0] = 0
        state = 0

        for end, char in enumerate(target, 1):
            while state and char not in children[state]:
                state = fail[state]
            state = children[state].get(char, 0)

            node = state
            while node != -1:
                item = terminal[node]
                if item is not None:
                    length, cost = item
                    dp[end] = min(dp[end], dp[end - length] + cost)
                node = output_link[node]

        return -1 if dp[-1] == inf else dp[-1]
