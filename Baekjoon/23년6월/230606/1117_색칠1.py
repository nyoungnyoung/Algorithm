def color():
    w, h, f, c, x1, y1, x2, y2 = map(int, input().split())
    x = w - f
    if x < w // 2:          # 접었을 때 왼쪽이 더 크면
        x = w - x
    fold = c + 1
    all = w * h             # 총 면적 
    fold = w - x
    n = x2 - x1
    if x1 < fold:
        if x2 > fold:       # x1은 포함, x2는 미포함일 때
            n += (fold - x1)
        else:               # x1, x2모두 포함일 때
            n *= 2
    print(all - (n * (y2 - y1) * fold))   

color()