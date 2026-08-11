# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:25Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        dependents = defaultdict(list)
        missing = {}

        for recipe, needed in zip(recipes, ingredients):
            missing[recipe] = len(needed)
            for ingredient in needed:
                dependents[ingredient].append(recipe)

        available = deque(supplies)
        answer = []
        while available:
            ingredient = available.popleft()
            for recipe in dependents[ingredient]:
                missing[recipe] -= 1
                if missing[recipe] == 0:
                    answer.append(recipe)
                    available.append(recipe)

        return answer
