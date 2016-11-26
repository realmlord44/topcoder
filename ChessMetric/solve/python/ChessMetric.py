def count(size, start, end, numMoves, ways):
    if numMoves < 1:
        if start == end:
            return 1
        else:
            return 0
    if ways[end[0]][end[1]][numMoves] == -1:
        ways[end[0]][end[1]][numMoves] = 0
        if end[1] + 2 < size and end[0] + 1 < size:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0]+1, end[1]+2], numMoves-1, ways)
        if end[1] + 1 < size and end[0] + 1 < size:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0]+1, end[1]+1], numMoves-1, ways)
        if end[1] + 1 < size:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0], end[1]+1], numMoves-1, ways)
        if end[0] + 1 < size:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0]+1, end[1]], numMoves-1, ways)
        if end[1] + 1 < size and end[0] + 2 < size:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0]+2, end[1]+1], numMoves-1, ways)
        if end[1] - 2 >= 0 and end[0] - 1 >= 0:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0]-1, end[1]-2], numMoves-1, ways)
        if end[1] - 1 >= 0 and end[0] - 1 >= 0:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0]-1, end[1]-1], numMoves-1, ways)
        if end[1] - 1 >= 0:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0], end[1]-1], numMoves-1, ways)
        if end[0] - 1 >= 0:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0]-1, end[1]], numMoves-1, ways)
        if end[1] - 1 >= 0 and end[0] - 2 >= 0:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0]-2, end[1]-1], numMoves-1, ways)
        if end[1] + 2 < size and end[0] - 1 >= 0:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0]-1, end[1]+2], numMoves-1, ways)
        if end[1] + 1 < size and end[0] - 1 >= 0:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0]-1, end[1]+1], numMoves-1, ways)
        if end[1] + 1 < size and end[0] - 2 >= 0:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0]-2, end[1]+1], numMoves-1, ways)
        if end[1] - 2 >= 0 and end[0] + 1 < size:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0]+1, end[1]-2], numMoves-1, ways)
        if end[1] - 1 >= 0 and end[0] + 1 < size:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0]+1, end[1]-1], numMoves-1, ways)
        if end[1] - 1 >= 0 and end[0] + 2 < size:
            ways[end[0]][end[1]][numMoves] += count(size, start, [end[0]+2, end[1]-1], numMoves-1, ways)
    return  ways[end[0]][end[1]][numMoves]

def howMany(size, start, end, numMoves):
    ways = [[[-1 for i in xrange(numMoves+1)] for j in xrange(size)] for k in xrange(size)]
    count(size, start, end, numMoves, ways)
    return ways[end[0]][end[1]][numMoves]
