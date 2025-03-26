"""
https://school.programmers.co.kr/learn/courses/30/lessons/49189

[ Queue & Stack ]

시작점은 1이므로 queue에 1을 euqueue 
path_list[i] = 1번 node에서 i번 node까지의 최단경로 ··· (1)

양방향 graph이므로 시작점과 도착점을 동시에 append해준다 
예를 들어 1번 노드가 4번과 5번 노드와 연결되어 있다면, 아래와 같다
graph = [[],[4,5],[],[],[1],[1]] ··· (2)

BFS로 Traverse 해준다 ··· (3)

현재 노드에서 연결된 노드 중에서 ··· (4)

방문한 적 없어야 하며 방문할 예정도 없어야 한다 
1번 노드가 아니면서 path_list의 값이 0이면 방문한 적 없는 것이고
queue에 없으면 방문 예정도 아닌 것이다 ··· (5)

이제 path_list의 max_value와 값이 같은 것이 몇 개인지 count하면 된다 ··· (6)
"""


from collections import deque
def solution(n, edge):
    queue=deque()
    # (1)
    queue.append(1)
    path_list=[0]*(n+1)
    graph =[[] for _ in range(n+1)]
    # (2)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    # (3)
    while queue:
        cur_node=queue.popleft()
        # (4)
        for candidate in graph[cur_node]:
            if candidate!=1:
                # (5)
                if path_list[candidate]==0 and candidate not in queue:
                    queue.append(candidate)
                    path_list[candidate]=path_list[cur_node]+1
    max_value = max(path_list)
    #print(path_list)
    answer=0
    # (6)
    for i in range(len(path_list)):
        if path_list[i]==max_value:
            answer+=1
    return answer
# arr=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# print(solution(6,arr))