# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:35Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        rook_can_capture = (a == e and not (c == a and min(b, f) < d < max(b, f))) or (
            b == f and not (d == b and min(a, e) < c < max(a, e))
        )
        bishop_can_capture = abs(c - e) == abs(d - f) and not (
            abs(a - c) == abs(b - d)
            and min(c, e) < a < max(c, e)
            and min(d, f) < b < max(d, f)
        )
        return 1 if rook_can_capture or bishop_can_capture else 2
