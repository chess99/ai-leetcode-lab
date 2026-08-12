# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:48Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from typing import List


class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms.sort(key=lambda room: room[1], reverse=True)
        ordered_queries = sorted(
            ((minimum_size, preferred, index)
             for index, (preferred, minimum_size) in enumerate(queries)),
            reverse=True)
        answer = [-1] * len(queries)
        room_ids = sorted(room_id for room_id, _ in rooms)
        positions = {room_id: index + 1 for index, room_id in enumerate(room_ids)}
        tree = [0] * (len(room_ids) + 1)

        def add(index):
            while index < len(tree):
                tree[index] += 1
                index += index & -index

        def prefix(index):
            count = 0
            while index:
                count += tree[index]
                index -= index & -index
            return count

        def kth(order):
            index = 0
            bit = 1 << (len(tree).bit_length() - 1)
            while bit:
                following = index + bit
                if following < len(tree) and tree[following] < order:
                    index = following
                    order -= tree[following]
                bit >>= 1
            return room_ids[index]

        room_index = 0
        for minimum_size, preferred, query_index in ordered_queries:
            while (room_index < len(rooms) and
                   rooms[room_index][1] >= minimum_size):
                add(positions[rooms[room_index][0]])
                room_index += 1
            left_count = prefix(bisect_right(room_ids, preferred))
            total_count = prefix(len(room_ids))
            candidates = []
            if left_count:
                candidates.append(kth(left_count))
            if left_count < total_count:
                candidates.append(kth(left_count + 1))
            if candidates:
                answer[query_index] = min(
                    candidates, key=lambda room_id: (abs(room_id - preferred), room_id))
        return answer
