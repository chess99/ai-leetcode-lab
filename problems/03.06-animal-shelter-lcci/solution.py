# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:56:59Z
# Experiment: ai-leetcode-lab, round 1
class AnimalShelf:

    def __init__(self):
        self.animals = []

    def enqueue(self, animal: List[int]) -> None:
        self.animals.append(animal)

    def dequeueAny(self) -> List[int]:
        return self.animals.pop(0) if self.animals else [-1, -1]

    def dequeueDog(self) -> List[int]:
        return self._dequeue_type(1)

    def dequeueCat(self) -> List[int]:
        return self._dequeue_type(0)

    def _dequeue_type(self, animal_type: int) -> List[int]:
        for index, animal in enumerate(self.animals):
            if animal[1] == animal_type:
                return self.animals.pop(index)
        return [-1, -1]


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()
