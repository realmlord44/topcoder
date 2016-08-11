def longestZigZag(sequence):
    longest = [1 for i in xrange(len(sequence))]
    lastAdded = [0 for i in xrange(len(sequence))]

    if len(sequence) > 1:
        if sequence[1] != sequence[0]:
            longest[1] = 2
            lastAdded[1] = 1

    for idx, i in enumerate(sequence[2:]):
        longest[idx+2] = longest[idx+1]
        lastAdded[idx+2] = lastAdded[idx+1]

        lastDiff = sequence[lastAdded[idx+1]] - sequence[lastAdded[lastAdded[idx+1]-1]]
        thisDiff = i - sequence[lastAdded[idx+1]]
        if thisDiff > 0 and lastDiff <= 0 or thisDiff < 0 and lastDiff >= 0:
            longest[idx+2] = longest[idx+1] + 1
            lastAdded[idx+2] = idx+2
        elif thisDiff > 0 and lastDiff > 0 or thisDiff < 0 and lastDiff < 0:
            lastAdded[idx+2] = idx+2

    return longest[-1]
