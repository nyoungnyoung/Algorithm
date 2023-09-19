def solution(n, costs):
    
    # find 연산
    def find(parent, n):
        # index값과 value값이 동일한지 확인
        if parent[n] != n:
            parent[n] = find(parent, parent[n])
        # 동일하면(if문에 걸리지 않으면) value값 return
        return parent[n]
    
    # union 연산
    def union(parent, a, b):
        # a, b중 작은 수를 대표노드로 설정
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[a] = b
        else:
            parent[b] = a
    
    answer = 0
    # costs를 비용 기준으로 오름차순 정렬
    costs.sort(key = lambda x: x[2])
    parent = [i for i in range(n)]
    
    # 가중치(비용)가 낮은 엣지부터 연결시도
    for a, b, cost in costs:
        # 사이클 없으면 union 연산으로 연결하고 비용 answer에 더해주기
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost
            
    return answer