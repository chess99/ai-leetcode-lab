# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:51:59Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from collections import defaultdict
from typing import List
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.price = {}
        self.available = defaultdict(list)
        self.rented = []
        self.is_rented = set()
        self.version = {}
        for shop, movie, price in entries:
            key = (shop, movie)
            self.price[key] = price
            self.version[key] = 0
            heapq.heappush(self.available[movie], (price, shop, 0))

    def search(self, movie: int) -> List[int]:
        heap=self.available[movie];answer=[];held=[]
        while heap and len(answer)<5:
            price,shop,version=heapq.heappop(heap)
            key=(shop,movie)
            if key not in self.is_rented and self.version[key]==version:
                answer.append(shop);held.append((price,shop,version))
        for item in held:heapq.heappush(heap,item)
        return answer

    def rent(self, shop: int, movie: int) -> None:
        key=(shop,movie)
        self.version[key]+=1
        self.is_rented.add(key)
        heapq.heappush(self.rented,(self.price[key],shop,movie,self.version[key]))

    def drop(self, shop: int, movie: int) -> None:
        key=(shop,movie)
        self.version[key]+=1
        self.is_rented.remove(key)
        heapq.heappush(self.available[movie],(self.price[key],shop,self.version[key]))

    def report(self) -> List[List[int]]:
        answer=[];held=[]
        while self.rented and len(answer)<5:
            price,shop,movie,version=heapq.heappop(self.rented)
            key=(shop,movie)
            if key in self.is_rented and self.version[key]==version:
                answer.append([shop,movie]);held.append((price,shop,movie,version))
        for item in held:heapq.heappush(self.rented,item)
        return answer


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
