def solution(wallpaper):
    x1, y1, x2, y2 = None,None,None,None

    for i,v in enumerate(wallpaper):
        for j,s in enumerate(v):
            if s == "#":
                x1 = x1 if x1 is not None and x1 < i else i
                y1 = y1 if y1 is not None and y1 < j else j

                x2 = x2 if x2 is not None and x2 > i else i
                y2 = y2 if y2 is not None and y2 > j else j

    return [x1, y1, x2+1, y2+1]

# solution([".#...", "..#..", "...#."])
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))