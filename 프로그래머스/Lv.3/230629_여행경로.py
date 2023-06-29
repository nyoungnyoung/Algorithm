from collections import defaultdict

def solution(tickets):
    # tickets 알파벳 순서대로 정렬해주기
    tickets.sort(key=lambda x:(x[0], x[1]))
    visited = [0] * len(tickets)
    answer = []
    # dfs 함수 만들어주기
    def dfs(s, path):
        # path가 tickets길이 + 1이 되면 모든 티켓 사용한 것!
        if len(path) == len(tickets) + 1:
            # answer에 path 추가해준 후 return
            answer.append(path)
            return
        # tickets 돌면서 dfs 수행해보기
        for idx, ticket in enumerate(tickets):
            # 해당 티켓을 사용한 적 없고, 시작지점과 ticket의 출발점이 같으면
            if not visited[idx] and ticket[0] == s:
                # 방문처리
                visited[idx] = 1
                # 해당 티켓의 목적지에서 dfs 다시 수행
                dfs(ticket[1], path + [ticket[1]])
                # dfs에서 모든 경로 다 돌지 못하면 idx 다시 초기화해주기
                visited[idx] = 0
    dfs('ICN', ['ICN'])
    return answer[0]

