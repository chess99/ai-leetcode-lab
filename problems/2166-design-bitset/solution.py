# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:30Z
# Experiment: ai-leetcode-lab, round 1
class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bits = [0] * size
        self.flipped = False
        self.ones = 0

    def fix(self, idx: int) -> None:
        if (self.bits[idx] ^ self.flipped) == 0:
            self.bits[idx] = 0 if self.flipped else 1
            self.ones += 1

    def unfix(self, idx: int) -> None:
        if (self.bits[idx] ^ self.flipped) == 1:
            self.bits[idx] = 1 if self.flipped else 0
            self.ones -= 1

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return "".join(
            "1" if bit ^ self.flipped else "0" for bit in self.bits
        )


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
