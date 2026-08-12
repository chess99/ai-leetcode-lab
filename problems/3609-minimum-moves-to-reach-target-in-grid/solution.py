# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        if sx > tx or sy > ty:
            return -1
        if tx == 0:
            if sx != 0 or sy == 0 or ty % sy:
                return 0 if (sx, sy) == (tx, ty) else -1
            ratio = ty // sy
            return ratio.bit_length() - 1 if ratio > 0 and ratio & (ratio - 1) == 0 else -1
        if ty == 0:
            if sy != 0 or sx == 0 or tx % sx:
                return 0 if (sx, sy) == (tx, ty) else -1
            ratio = tx // sx
            return ratio.bit_length() - 1 if ratio > 0 and ratio & (ratio - 1) == 0 else -1
        moves = 0
        while (tx, ty) != (sx, sy):
            if tx < sx or ty < sy or (tx == 0 and ty == 0):
                return -1
            if tx > ty:
                # If x was already the larger coordinate it was doubled;
                # otherwise the old maximum was y and x is reduced by y.
                if tx > 2 * ty:
                    if tx & 1: return -1
                    tx //= 2; moves += 1
                else:
                    tx -= ty; moves += 1
            elif ty > tx:
                if ty > 2 * tx:
                    if ty & 1: return -1
                    ty //= 2; moves += 1
                else:
                    ty -= tx; moves += 1
            else:
                # Equal positive coordinates can only have been reached from
                # (0,x) or (x,0); normal reverse subtraction would loop.
                if sx == tx and sy == ty:
                    return moves
                candidates = []
                if sx == 0 and sy and tx % sy == 0:
                    r = tx // sy
                    if r & (r - 1) == 0: candidates.append(moves + r.bit_length())
                if sy == 0 and sx and ty % sx == 0:
                    r = ty // sx
                    if r & (r - 1) == 0: candidates.append(moves + r.bit_length())
                return min(candidates) if candidates else -1
        return moves
