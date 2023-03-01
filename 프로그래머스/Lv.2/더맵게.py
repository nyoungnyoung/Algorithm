import heapq

def solution(scoville, K):
    # heapq로 만드는 힙은 기본적으로 루트노드가 가장 작은 최소힙
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:      # 값이 가장 작은 루트노드가 K이상이 될때까지 반복
        min_1, min_2 = heapq.heappop(scoville), heapq.heappop(scoville)     # 값이 가장 작은 2개의 음식 pop
        mix = min_1 + (min_2 * 2)       # 섞어주기
        heapq.heappush(scoville, mix)   # 섞은 음식의 스코빌 지수 다시 힙에 넣어주기 
        answer += 1
        # 음식이 하나 남을때까지 섞었는데도 스코빌지수가 K보다 작으면 -1 return
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer