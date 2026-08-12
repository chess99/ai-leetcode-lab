# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:46Z
# Experiment: ai-leetcode-lab, round 1
class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        index += 1
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, end: int) -> int:
        total = 0
        while end:
            total += self.tree[end]
            end -= end & -end
        return total

    def range_sum(self, left: int, right: int) -> int:
        return self.prefix_sum(right) - self.prefix_sum(left)

    def kth(self, order: int) -> int:
        index = 0
        step = 1 << (self.size.bit_length() - 1)
        while step:
            candidate = index + step
            if candidate <= self.size and self.tree[candidate] < order:
                index = candidate
                order -= self.tree[candidate]
            step >>= 1
        return index


class BlackBox:

    def __init__(self, n: int, m: int):
        self.height = n
        self.width = m
        self.perimeter = 2 * (n + m)
        coordinates = [self._coordinate(index) for index in range(self.perimeter)]
        coordinate_to_index = {coordinate: index for index, coordinate in enumerate(coordinates)}

        states = []
        state_id = {}
        vectors = {}
        for index, (x, y) in enumerate(coordinates):
            for direction in (-1, 1):
                vector = self._inward_vector(x, y, direction)
                if vector is not None:
                    state_id[(index, direction)] = len(states)
                    vectors[len(states)] = vector
                    states.append((index, direction))

        transition = [0] * len(states)
        for current, (index, _) in enumerate(states):
            x, y = coordinates[index]
            dx, dy = vectors[current]
            horizontal = self.width - x if dx > 0 else x
            vertical = self.height - y if dy > 0 else y
            travel = min(horizontal, vertical)
            next_x, next_y = x + dx * travel, y + dy * travel
            if next_x in (0, self.width):
                dx = -dx
            if next_y in (0, self.height):
                dy = -dy
            next_index = coordinate_to_index[(next_x, next_y)]
            transition[current] = state_id[(next_index, dy // dx)]

        self.state_position = [0] * len(states)
        self.cycle_bounds = [None] * len(states)
        self.flat_state = []
        visited = [False] * len(states)
        for start in range(len(states)):
            if visited[start]:
                continue
            cycle = []
            current = start
            while not visited[current]:
                visited[current] = True
                cycle.append(current)
                current = transition[current]
            begin = len(self.flat_state)
            self.flat_state.extend(cycle)
            end = len(self.flat_state)
            for offset, state in enumerate(cycle):
                self.state_position[state] = begin + offset
                self.cycle_bounds[state] = (begin, end)

        self.state_id = state_id
        self.states = states
        self.positions_by_hole = [[] for _ in range(self.perimeter)]
        for state, (index, _) in enumerate(states):
            self.positions_by_hole[index].append(self.state_position[state])
        self.opened = [False] * self.perimeter
        self.active = FenwickTree(len(states))


    def open(self, index: int, direction: int) -> int:
        if not self.opened[index]:
            self.opened[index] = True
            for position in self.positions_by_hole[index]:
                self.active.add(position, 1)

        state = self.state_id[(index, direction)]
        position = self.state_position[state]
        begin, end = self.cycle_bounds[state]
        after_count = self.active.range_sum(position + 1, end)
        if after_count:
            order = self.active.prefix_sum(position + 1) + 1
        else:
            order = self.active.prefix_sum(begin) + 1
        next_position = self.active.kth(order)
        next_state = self.flat_state[next_position]
        return self.states[next_state][0]


    def close(self, index: int) -> None:
        self.opened[index] = False
        for position in self.positions_by_hole[index]:
            self.active.add(position, -1)

    def _coordinate(self, index: int):
        if index <= self.width:
            return index, self.height
        index -= self.width
        if index <= self.height:
            return self.width, self.height - index
        index -= self.height
        if index <= self.width:
            return self.width - index, 0
        index -= self.width
        return 0, index

    def _inward_vector(self, x: int, y: int, direction: int):
        for dx, dy in ((1, direction), (-1, -direction)):
            if x == 0 and dx <= 0:
                continue
            if x == self.width and dx >= 0:
                continue
            if y == 0 and dy <= 0:
                continue
            if y == self.height and dy >= 0:
                continue
            return dx, dy
        return None



# Your BlackBox object will be instantiated and called as such:
# obj = BlackBox(n, m)
# param_1 = obj.open(index,direction)
# obj.close(index)
