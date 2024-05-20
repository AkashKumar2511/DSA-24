"""
Algorithm:
---------
1. Use a boolean list to mark all the vertices as not visited.
2. Initially mark first vertex as visited(true).
3. Create a queue for BFS and push first vertex in queue.
4. While queue is not empty:
   I. Keep adding front element in output list and popping it from queue.
   II. Traverse over all the connected components of front element.
   III. If they aren't visited, mark them visited and add to queue.
5. Return the output list.


Time Complexity: O(V + E)
Space Complexity: O(V)
"""


#starting node : 0
def bfs(adj, start):
  vis = [start] * v
  queue = [start]
  ans = []
  vis[start] = 1
  
  while(queue):
      x = queue.pop(0)
      ans.append(x)
      
      for i in adj[x]:
          if(not vis[i]):
              vis[i] = 1
              queue.append(i)
              
  return ans
