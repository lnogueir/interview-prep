'''
Prompt:

Given a graph, a source node v1, and a destination node v2,
find the shortest between node v1 and v2.
'''

def minimumPath(graph, v1, v2):
  distances = [float('inf') for _ in range(len(graph))]
  distances[v1] = 0
  visited = [False for _ in range(len(graph))]

  queue = [v1]
  while len(queue) > 0:
    v = queue.pop()
    for neighbour in graph[v]:
      distances[neighbour] = min(distances[neighbour], distances[v] + 1)
      if not visited[neighbour]:
        queue.append(neighbour)

    visited[v] = True

  return distances[v2]

graph1 = [
  [1, 3],
  [0,3,2],
  [1],
  [0, 1]
]

graph2 = [
  [1,2],
  [2,3],
  [1,3],
  [4],
  []
]

print(minimumPath(graph1, 0, 3))
print(minimumPath(graph2, 0, 4))


