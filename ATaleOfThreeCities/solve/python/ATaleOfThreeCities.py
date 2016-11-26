import math
def connect(ax, ay, bx, by, cx, cy):
    dists = [
        (set((0, 1)), (aidx, bidx), math.sqrt((ax[aidx]-bx[bidx]) * (ax[aidx]-bx[bidx]) + (ay[aidx]-by[bidx]) * (ay[aidx]-by[bidx])))
        for bidx in xrange(len(bx)) for aidx in xrange(len(ax))
    ]
    dists.extend([
        (set((0, 2)), (aidx, cidx), math.sqrt((ax[aidx]-cx[cidx]) * (ax[aidx]-cx[cidx]) + (ay[aidx]-cy[cidx]) * (ay[aidx]-cy[cidx])))
        for cidx in xrange(len(cx)) for aidx in xrange(len(ax))
    ])
    dists.extend([
        (set((1, 2)), (bidx, cidx), math.sqrt((bx[bidx]-cx[cidx]) * (bx[bidx]-cx[cidx]) + (by[bidx]-cy[cidx]) * (by[bidx]-cy[cidx])))
        for cidx in xrange(len(cx)) for bidx in xrange(len(bx))
    ])
    dists.sort(key=lambda x: x[2])
    missing = set((0, 1, 2)).difference(dists[0][0]).pop()
    for item in dists[1:]:
        if missing in item[0]:
            return item[2]+dists[0][2]
