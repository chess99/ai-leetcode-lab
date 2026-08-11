# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:20Z
# Experiment: ai-leetcode-lab, round 1
class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.direction = 0
        self.directions = ['East', 'North', 'West', 'South']
        self.delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def step(self, num: int) -> None:
        perimeter = 2 * (self.width + self.height) - 4
        moves = num % perimeter or perimeter

        for _ in range(moves):
            dx, dy = self.delta[self.direction]
            next_x, next_y = self.x + dx, self.y + dy
            if not (0 <= next_x < self.width and 0 <= next_y < self.height):
                self.direction = (self.direction + 1) % 4
                dx, dy = self.delta[self.direction]
                next_x, next_y = self.x + dx, self.y + dy
            self.x, self.y = next_x, next_y

    def getPos(self):
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.directions[self.direction]
