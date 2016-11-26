solns = set(())

def isValid(st):
    open = 0
    for let in st:
        if let == '(':
            open += 1
        else:
            open -= 1
            if open < 0:
                return 0
    if open == 0:
        return 1
    return 0

def help(moves, s):
    movesKey = tuple(moves)
    if len(moves) == 1:
        if (movesKey, s) not in solns:
            solns.add((movesKey, s))
            res = isValid(s)
            if s[moves[0]] != s[moves[0] + 1]:
                res += isValid(s[:moves[0]] + s[moves[0] + 1] + s[moves[0]] + s[moves[0] + 2:])
            return res
        return 0
    else:
        # skip move
        count = 0 if (movesKey, s) in solns else help(moves[1:], s)

        # apply this move if it does something
        if s[moves[0]] != s[moves[0] + 1]:
            news = s[:moves[0]] + s[moves[0] + 1] + s[moves[0]] + s[moves[0] + 2:]
            count += 0 if (movesKey, s) in solns else help(moves[1:], news)
    solns.add((movesKey, s))
    return count

def countValid(s, op):
    res = help(op, s)
    return res
