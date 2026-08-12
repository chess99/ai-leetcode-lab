# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n=n;self.d=[[10**15]*n for _ in range(n)]
        for i in range(n):self.d[i][i]=0
        for a,b,w in edges:self.d[a][b]=min(self.d[a][b],w)
        for k in range(n):
            for i in range(n):
                for j in range(n):self.d[i][j]=min(self.d[i][j],self.d[i][k]+self.d[k][j])

    def addEdge(self, edge: List[int]) -> None:
        a,b,w=edge
        for i in range(self.n):
            for j in range(self.n):self.d[i][j]=min(self.d[i][j],self.d[i][a]+w+self.d[b][j])

    def shortestPath(self, node1: int, node2: int) -> int:
        return -1 if self.d[node1][node2]>=10**15 else self.d[node1][node2]


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
