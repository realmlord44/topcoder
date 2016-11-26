import pprint

def help(i, j, maxim, donations):
    if i > j:
        return 0
    if maxim[i][j] == 0:
        if j-i < 2:
            maxim[i][j] = max(donations[i:j+1])
        else:
            # check the leftmost two with the helper
            leftmax = donations[i] + help(i+2, j, maxim, donations)
            rightmax = donations[i+1] + help(i+3, j, maxim, donations)
            # print i, j, leftmax, rightmax
            maxim[i][j] = max(leftmax, rightmax)
    # print 'help(%i, %i)' % (i, j), maxim[i][j]
    return maxim[i][j]

def maxDonations(donations):
    print ''
    if len(donations) <= 3:
        return max(donations)
    maxim = [[donations[i] if i == j else 0 for i in xrange(len(donations))] for j in xrange(len(donations))]
    maxim[0][-1] = max(donations[0] + help(2, len(donations) - 2, maxim, donations), donations[1] + help(3, len(donations)-1, maxim, donations), donations[-1] + help(1, len(donations)-3, maxim, donations))
    '''
    print ''
    for i in maxim:
        print i
    print ''
    '''
    return maxim[0][-1]
