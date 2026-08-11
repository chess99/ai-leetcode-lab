# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:49:29Z
# Experiment: ai-leetcode-lab, round 1
import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-count, char) for count, char in ((a,'a'),(b,'b'),(c,'c')) if count]
        heapq.heapify(heap); answer = []
        while heap:
            count, char = heapq.heappop(heap)
            if len(answer) >= 2 and answer[-1] == answer[-2] == char:
                if not heap: break
                other_count, other = heapq.heappop(heap)
                answer.append(other); other_count += 1
                if other_count: heapq.heappush(heap,(other_count,other))
                heapq.heappush(heap,(count,char))
            else:
                answer.append(char); count += 1
                if count: heapq.heappush(heap,(count,char))
        return ''.join(answer)
