# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Fenwick:
    def __init__(self, size: int) -> None:
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        index += 1
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, end: int) -> int:
        total = 0
        while end > 0:
            total += self.tree[end]
            end -= end & -end
        return total

    def kth(self, rank: int) -> int:
        index = 0
        step = 1 << (self.size.bit_length() - 1)
        while step:
            next_index = index + step
            if next_index <= self.size and self.tree[next_index] < rank:
                rank -= self.tree[next_index]
                index = next_index
            step >>= 1
        return index


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        breaks = Fenwick(n)
        length_count = Fenwick(n + 1)
        length_sum = Fenwick(n + 1)
        break_total = 0

        def distance(left: int, right: int) -> int:
            value = (right - left) % n
            return n if value == 0 else value

        def change_length(length: int, delta: int) -> None:
            length_count.add(length, delta)
            length_sum.add(length, delta * length)

        def predecessor(position: int) -> int:
            before = breaks.prefix_sum(position)
            rank = before if before else break_total
            return breaks.kth(rank)

        def successor(position: int) -> int:
            through = breaks.prefix_sum(position + 1)
            rank = through + 1 if through < break_total else 1
            return breaks.kth(rank)

        def add_break(position: int) -> None:
            nonlocal break_total
            if break_total == 0:
                change_length(n, 1)
            else:
                left = predecessor(position)
                right = successor(position)
                change_length(distance(left, right), -1)
                change_length(distance(left, position), 1)
                change_length(distance(position, right), 1)
            breaks.add(position, 1)
            break_total += 1

        def remove_break(position: int) -> None:
            nonlocal break_total
            if break_total == 1:
                change_length(n, -1)
            else:
                left = predecessor(position)
                right = successor(position)
                change_length(distance(left, position), -1)
                change_length(distance(position, right), -1)
                change_length(distance(left, right), 1)
            breaks.add(position, -1)
            break_total -= 1

        for index in range(n):
            if colors[index] == colors[(index + 1) % n]:
                add_break(index)

        answers = []
        for query in queries:
            if query[0] == 1:
                size = query[1]
                if break_total == 0:
                    answers.append(n)
                else:
                    short_count = length_count.prefix_sum(size)
                    short_sum = length_sum.prefix_sum(size)
                    count = break_total - short_count
                    total = n - short_sum
                    answers.append(total - (size - 1) * count)
                continue

            index, color = query[1], query[2]
            if colors[index] == color:
                continue
            affected = {(index - 1) % n, index}
            old = {edge: colors[edge] == colors[(edge + 1) % n] for edge in affected}
            colors[index] = color
            for edge in affected:
                new_is_break = colors[edge] == colors[(edge + 1) % n]
                if old[edge] and not new_is_break:
                    remove_break(edge)
                elif not old[edge] and new_is_break:
                    add_break(edge)

        return answers
