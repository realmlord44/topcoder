import itertools
best = {}
ref = (9, 3, 1)
def solve(x, attacks):
    try:
        return best[x]
    except:
        best[x] = 500
        if all((i <= 0 for i in x)):
            if attacks < best[x]:
                best[x] = attacks
        else:
            best[x] = min(
                (
                    solve(tuple(x[i] - tup[i] for i in xrange(len(x))),
                          attacks + 1)
                    for tup in itertools.permutations(ref[:len(x)])
                    if not any(x[i] <= 0 and tup[i] == 9 for i in xrange(len(x)))
                )
            )
        return best[x]

def minimalAttacks(x):
    return min((solve(tuple((x[i] - tup[i] for i in xrange(len(x)))), 1) for tup in itertools.permutations(ref[:len(x)])))

