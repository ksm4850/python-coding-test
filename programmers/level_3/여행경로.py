def solution(tickets):
  answer = []
  
  visited = [False] * len(tickets)
  def dfs(airport ,path):
    if len(path) == len(tickets)+1:
      answer.append(path)
      return
    
    for i,ticket in enumerate(tickets):
      if ticket[0] == airport and not visited[i]:
        visited[i] = True
        dfs(ticket[1], path + [ticket[1]])
        visited[i] = False
        
  dfs("ICN",["ICN"])

  answer.sort()

  return answer[0]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))