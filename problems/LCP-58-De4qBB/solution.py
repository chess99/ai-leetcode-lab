# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: high
# Profile: sol-high
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def composeCube(self, shapes: List[List[str]]) -> bool:
        n = len(shapes[0])
        shell_size = n ** 3 - max(0, n - 2) ** 3
        if sum(row.count("1") for shape in shapes for row in shape) != shell_size:
            return False

        def variants(shape: List[str]):
            a = tuple(shape)
            result = set()
            for _ in range(4):
                result.add(a)
                result.add(tuple(row[::-1] for row in a))
                a = tuple("".join(a[n - 1 - c][r] for c in range(n)) for r in range(n))
            return result

        def position(face: int, r: int, c: int) -> int:
            if face == 0:
                x, y, z = r, c, 0
            elif face == 1:
                x, y, z = r, c, n - 1
            elif face == 2:
                x, y, z = 0, r, c
            elif face == 3:
                x, y, z = n - 1, r, c
            elif face == 4:
                x, y, z = r, 0, c
            else:
                x, y, z = r, n - 1, c
            return (x * n + y) * n + z

        placements = [[[] for _ in range(6)] for _ in range(6)]
        for piece, shape in enumerate(shapes):
            for face in range(6):
                masks = set()
                for form in variants(shape):
                    mask = 0
                    for r in range(n):
                        for c in range(n):
                            if form[r][c] == "1":
                                mask |= 1 << position(face, r, c)
                    masks.add(mask)
                placements[piece][face] = tuple(masks)

        # A rotation/reflection of the entire cube can put piece 0 in this
        # exact pose, so fixing it removes 48 symmetric search branches.
        first = placements[0][0][0]

        def dfs(used_pieces: int, used_faces: int, occupied: int) -> bool:
            if used_faces == 0b111111:
                return True

            best_face = -1
            best_options = None
            for face in range(1, 6):
                if used_faces >> face & 1:
                    continue
                options = []
                for piece in range(1, 6):
                    if used_pieces >> piece & 1:
                        continue
                    for mask in placements[piece][face]:
                        if occupied & mask == 0:
                            options.append((piece, mask))
                if not options:
                    return False
                if best_options is None or len(options) < len(best_options):
                    best_face, best_options = face, options

            for piece, mask in best_options:
                if dfs(
                    used_pieces | (1 << piece),
                    used_faces | (1 << best_face),
                    occupied | mask,
                ):
                    return True
            return False

        return dfs(1, 1, first)
