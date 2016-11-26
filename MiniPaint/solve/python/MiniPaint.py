BIG = 3000

def stripScore(i, row, cache, start, needed, prev):
    if needed > 0 and start >= len(row[0]):
        return BIG
    if needed == 0 or start >= len(row[0]):
        return 0
    if cache[i][prev][start][needed] != -1:
        return cache[i][prev][start][needed]
    best = BIG
    for j in xrange(3):
        newneed = needed
        add = 0
        if j == 0 or j == prev:
            newneed -= 1
        if j == 0 or j != row[1][start]:
            add += row[0][start]
        best = min(best, stripScore(i, row, cache, start + 1, newneed, j) + add)
    cache[i][prev][start][needed] = min(BIG, best)
    return cache[i][prev][start][needed]

def leastBad(picture, maxStrokes):
    if maxStrokes == 0:
        return len(picture) * len(picture[0])
    reqStrokes = 0
    for i in xrange(len(picture)):
        reqStrokes += 1
        for j in xrange(len(picture[i]) - 1):
            if picture[i][j] != picture[i][j+1]:
                reqStrokes += 1
    if maxStrokes >= reqStrokes:
        return 0

    rows = [[[],[]] for i in picture]
    for i in xrange(len(picture)):
        last = picture[i][0]
        leng = 0
        for j in picture[i]:
            if last == j:
                leng += 1
            else:
                rows[i][0].append(leng)
                rows[i][1].append(last)
                leng = 1
                last = j
        rows[i][0].append(leng)
        rows[i][1].append(last)

    rcache = [[[[-1 for i in xrange(51)] for j in xrange(50)] for k in xrange(3)] for l in xrange(len(picture))]

    for i in xrange(len(picture)):
        stripScore(i, rows[i], rcache, 0, 50, 0)

    print rcache[0]
    return 1
