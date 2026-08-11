# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:29Z
# Experiment: ai-leetcode-lab, round 1

from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_heaps = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            heappush(self.cuisine_heaps[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food]
        heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]
        while -heap[0][0] != self.food_to_rating[heap[0][1]]:
            heappop(heap)
        return heap[0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food, newRating)
# param_2 = obj.highestRated(cuisine)
