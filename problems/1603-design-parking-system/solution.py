# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:10:54Z
# Experiment: ai-leetcode-lab, round 1
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.spaces[carType]:
            self.spaces[carType] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
