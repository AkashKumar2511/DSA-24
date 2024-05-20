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
