from collections import deque

#data = sys.stdin.read().splitlines()
data = []
try:
    while True:
        line = input()
        if line == EOFError:
            break
        data.append(line)
except EOFError:
    pass
#print(data)
if not data:
     print("NO")
     exit(0)

start = data[-2].strip()
end = data[-1].strip()

# print(start)
# print(end)
if start == end:
    print("YES")
    exit(0)

graph = {}
for i in range(len(data) - 2):
    line = data[i].strip()
    #print(f"line = {line}")
    parts = line.split()
    a, b = parts[0], parts[1]
    if a not in graph:
        graph[a] = set()
    if b not in graph:
        graph[b] = set()
    graph[a].add(b)
    graph[b].add(a)


visited = set()
queue = deque([start])
visited.add(start)
#print(f"graph: {graph}")
while queue:
    node = queue.popleft()
    if node == end:
        print("YES")
        exit(0)
    for neighbor in graph.get(node, []):
        #print(graph.get(node,[]))
        #print(f"node = {node} neighbor = {neighbor}")
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

print("NO")
