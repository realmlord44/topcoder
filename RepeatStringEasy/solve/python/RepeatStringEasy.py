def LCS(a, b):
    best = [[0 for i in b] for j in a]
    z = 0
    for i in xrange(len(a)):
        for j in xrange(len(b)):
            if a[i] == b[j]:
                best[i][j] = best[i-1][j-1] + 1 if i > 0 and j > 0 else 1
            else:
                best[i][j] = max(best[i][j-1], best[i-1][j]) if i > 0 and j > 0 else best[i][j-1] if j > 0 else best[i-1][j] if i > 0 else 0
            if best[i][j] > z:
                z = best[i][j]
    return z

def maximalLength(s):
    if len(s) < 2:
        return 0
    # find first repeat
    letters = {
        s[0]: 1,
    }
    repeat = False
    for let in s[1:]:
        try:
            letters[let] += 1
        except:
            letters[let] = 1
    shortstr = [let for let in s if letters[let] > 1]
    try:
        return max((LCS(shortstr[:x], shortstr[x:]) for x in xrange(1, len(shortstr)))) * 2
    except:
        return 0
