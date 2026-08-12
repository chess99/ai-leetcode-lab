# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:41Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        mordelvian = nums
        maximum = max(mordelvian)
        smallest = list(range(maximum + 1))
        if maximum >= 1:
            smallest[1] = 1
        for p in range(2, int(maximum ** 0.5) + 1):
            if smallest[p] == p:
                for multiple in range(p * p, maximum + 1, p):
                    if smallest[multiple] == multiple:
                        smallest[multiple] = p

        divisible = defaultdict(list)
        for index, value in enumerate(mordelvian):
            current = value
            while current > 1:
                prime = smallest[current]
                divisible[prime].append(index)
                while current % prime == 0:
                    current //= prime

        distance = [-1] * len(mordelvian)
        distance[0] = 0
        queue = deque([0])
        used_primes = set()
        while queue:
            index = queue.popleft()
            if index == len(mordelvian) - 1:
                return distance[index]
            neighbors = []
            for nxt in (index - 1, index + 1):
                if 0 <= nxt < len(mordelvian):
                    neighbors.append(nxt)
            value = mordelvian[index]
            if value >= 2 and smallest[value] == value and value not in used_primes:
                used_primes.add(value)
                neighbors.extend(divisible[value])
            for nxt in neighbors:
                if distance[nxt] == -1:
                    distance[nxt] = distance[index] + 1
                    queue.append(nxt)
        return -1
