def solution(sizes):
    w = []
    h = []
    for size in sizes:
        if size[0] > size[1]: # 큰값을 w, 작은값을 h에 저장
            w.append(size[0])
            h.append(size[1])
        else:
            h.append(size[0])
            w.append(size[1])

    return max(w) * max(h)