# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def gobang(self, pieces: List[List[int]]) -> str:
        occupied = {(x, y): color for x, y, color in pieces}
        directions = ((1, 0), (0, 1), (1, 1), (1, -1))

        def wins(point, color: int, extra=None) -> bool:
            x, y = point

            def is_color(px: int, py: int) -> bool:
                if extra == (px, py):
                    return color == 0
                return occupied.get((px, py)) == color

            for dx, dy in directions:
                count = 1
                step = 1
                while is_color(x + dx * step, y + dy * step):
                    count += 1
                    step += 1
                step = 1
                while is_color(x - dx * step, y - dy * step):
                    count += 1
                    step += 1
                if count >= 5:
                    return True
            return False

        def candidate_moves(color: int):
            candidates = set()
            for x, y, piece_color in pieces:
                if piece_color != color:
                    continue
                for dx, dy in directions:
                    for distance in range(-4, 5):
                        point = (x + dx * distance, y + dy * distance)
                        if point not in occupied:
                            candidates.add(point)
            return candidates

        black_candidates = candidate_moves(0)
        black_wins = {point for point in black_candidates if wins(point, 0)}
        if black_wins:
            return "Black"

        white_candidates = candidate_moves(1)
        white_wins = {point for point in white_candidates if wins(point, 1)}
        if len(white_wins) >= 2:
            return "White"

        first_moves = white_wins if white_wins else black_candidates
        for first_move in first_moves:
            if first_move in occupied:
                continue
            threats = set()
            x, y = first_move
            for dx, dy in directions:
                for distance in range(-4, 5):
                    point = (x + dx * distance, y + dy * distance)
                    if point == first_move or point in occupied:
                        continue
                    if wins(point, 0, first_move):
                        threats.add(point)
                        if len(threats) >= 2:
                            return "Black"
        return "None"
