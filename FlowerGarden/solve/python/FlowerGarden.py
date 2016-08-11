def getOrdering(height, bloom, wilt):
    res = [-1 for i in xrange(len(height))]
    used = [False for i in xrange(len(height))]
    print ''
    for i in xrange(len(height)):
        best = -1
        for j in xrange(len(height)):
            if not used[j]:
                ok = True
                for k in xrange(len(height)):
                    if k != j and not used[k] and wilt[k] >= bloom[j] and bloom[k] <= wilt[j] and height[j] > height[k]:
                        ok = False
                if ok and (best == -1 or height[j]>height[best]):
                    best = j
        res[i] = height[best]
        used[best] = True
    return res
