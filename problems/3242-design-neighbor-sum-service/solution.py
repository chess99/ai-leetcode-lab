# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:47:54Z
# Experiment: ai-leetcode-lab, round 1
class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.positions = {}
        for row, values in enumerate(grid):
            for col, value in enumerate(values):
                self.positions[value] = (row, col)

    def adjacentSum(self, value: int) -> int:
        row, col = self.positions[value]
        return self._sum_neighbors(row, col, ((-1, 0), (1, 0), (0, -1), (0, 1)))

    def diagonalSum(self, value: int) -> int:
        row, col = self.positions[value]
        return self._sum_neighbors(row, col, ((-1, -1), (-1, 1), (1, -1), (1, 1)))

    def _sum_neighbors(self, row: int, col: int, directions: tuple) -> int:
        n = len(self.grid)
        return sum(
            self.grid[row + dr][col + dc]
            for dr, dc in directions
            if 0 <= row + dr < n and 0 <= col + dc < n
        )


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
