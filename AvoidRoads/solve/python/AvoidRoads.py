def count(w, h, bad, ways):
    if ways[w][h] == -1:
        if '%i %i %i %i' % (w-1, h, w, h) not in bad and '%i %i %i %i' % (w, h, w-1, h) not in bad and w > 0:
            if ways[w][h] == -1:
                ways[w][h] = count(w-1, h, bad, ways)
            else:
                ways[w][h] += count(w-1, h, bad, ways)
        if '%i %i %i %i' % (w, h-1, w, h) not in bad and '%i %i %i %i' % (w, h, w, h-1) not in bad and h > 0:
            if ways[w][h] == -1:
                ways[w][h] = count(w, h-1, bad, ways)
            else:
                ways[w][h] += count(w, h-1, bad, ways)
        if ways[w][h] == -1:
            ways[w][h] = 0
    return ways[w][h]

def numWays(width, height, bad):
    ways = [[1 if i == 0 and j == 0 else -1 for i in xrange(height + 1)] for j in xrange(width + 1)]
    count(width, height, bad, ways)
    return ways[width][height]
