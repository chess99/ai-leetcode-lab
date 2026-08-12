# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:17Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from functools import lru_cache


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        colors = 'RYBGW'
        initial = Counter(hand)

        def shrink(state):
            changed = True
            while changed:
                changed = False
                index = 0
                pieces = []
                while index < len(state):
                    following = index + 1
                    while following < len(state) and state[following] == state[index]:
                        following += 1
                    if following - index >= 3:
                        changed = True
                    else:
                        pieces.append(state[index:following])
                    index = following
                state = ''.join(pieces)
            return state

        @lru_cache(None)
        def search(state, counts):
            state = shrink(state)
            if not state:
                return 0
            board_counts = Counter(state)
            if any(board_counts[color] + counts[index] < 3
                   for index, color in enumerate(colors) if board_counts[color]):
                return -1

            best = 6
            for color_index, color in enumerate(colors):
                if counts[color_index] == 0:
                    continue
                remaining = list(counts)
                remaining[color_index] -= 1
                remaining = tuple(remaining)
                next_states = set()
                for position in range(len(state) + 1):
                    # Positions inside the same run produce an identical board.
                    if position > 0 and state[position - 1] == color:
                        continue
                    following = shrink(state[:position] + color + state[position:])
                    if following in next_states:
                        continue
                    next_states.add(following)
                    rest = search(following, remaining)
                    if rest >= 0:
                        best = min(best, 1 + rest)
            return -1 if best == 6 else best

        return search(board, tuple(initial[color] for color in colors))
