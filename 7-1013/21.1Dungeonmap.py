from collections import deque
import sys

inp = sys.stdin.read().splitlines()
start = inp[-2]
end = inp[-1]
if end == start:
    print("YES")
    exit(0)
#print(inp)
graph = {}
for line in inp[:-2]:
    names = [name.strip() for name in line.split(' ')]
    a = names[0]
    b = names[1]
    if a not in graph:
        graph[a] = set()
    if b not in graph:
        graph[b] = set()
    graph[a].add(b)
    graph[b].add(a)

#print(graph)

visited = set()
queue = deque([start])
visited.add(start)
#print(visited)

while queue:
    node = queue.popleft()
    if node == end:
        print("YES")
        exit(0)
    for neighber in graph.get(node, []):
        if neighber == end:
            print("YES")
            exit(0)
        queue.append(neighber)
        visited.add(neighber)
print("NO")
