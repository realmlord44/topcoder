def genPalindrome(_str):
    if len(_str) < 2:
        return ''
    if len(_str) == 2:
        return _str[0:1] if _str[0] != _str[1] else ''

    orig = _str
    tail = []
    checkpoint = False
    last = 0
    left = 0
    right = len(_str) - 1
    while left < right:
        print 'comparing _str[%d] vs _str[%d].. %s vs %s..' % (left, right, _str[left], _str[right])
        if _str[left] != _str[right]:
            print '\tmismatch..'
            if checkpoint:
                toInject = _str[last:left + 1]
                print '\t\tinject str %s from checkpoint position %d to left position %d inclusive..' % (toInject, last, left)
                for letter in toInject:
                    tail.insert(0, letter)
                _str = orig + ''.join(tail)
                print '\t\tnew _str is %s' % _str
                right += (left - last)
                print '\t\tadjusting current right position to next comparison due to injection by %d.. now %d' % (left-last, right)
                last = left + 1
                print '\t\tsetting new checkpoint at position %d..' % last
                checkpoint = False
                print '\t\tclearing checkpoint flag..'
                left += 1
                print '\t\tincrementing left for next comparison.. now %d..' % left
            else:
                tail.insert(0, _str[left])
                print '\t\tmust append at least %s to end..' % ''.join(tail)
                _str = orig + ''.join(tail)
                print '\t\tnew _str is %s..' % _str
                left += 1
                print '\t\tincrementing left for next comparison.. now %d..' % left
                last = left
                print '\t\tsetting new checkpoint at position %d..' % last
                checkpoint = True

        else:
            print '\tmatch.. setting checkpoint flag and comparing next values..'
            checkpoint = True
            left += 1
            right -= 1
    print 'comparing middle value(s).. left: %d right: %d, %s vs %s .. match' % (left, right, _str[left], _str[right])

    return ''.join(tail)

"""
print 'abcedb', genPalindrome('abcedb')
print 'abcb', genPalindrome('abcb')
print 'abb', genPalindrome('abb')
print 'abccdb', genPalindrome('abccdb')
print 'abcddc', genPalindrome('abcddc')
"""


def g(_in):
    return _in + genPalindrome(_in)


def test(_in, _expected):
    print _in
    actual = g(_in)
    print "actual", actual, "expected", _expected
    print "pass" if actual == _expected else "fail"
    print


test('aa', 'aa')
test('madamim', 'madamimadam')
test('amanaplan', 'amanaplanalpanama')
test('amanaplana', 'amanaplanalpanama')
test('amanaplanal', 'amanaplanalpanama')
test('amanaplanalp', 'amanaplanalpanama')
test('amanaplanalpa', 'amanaplanalpanama')
test('amanaplanalpan', 'amanaplanalpanama')
test('amanaplanalpana', 'amanaplanalpanama')
test('amanaplanalpanam', 'amanaplanalpanama')
test('amanaplanalpanama', 'amanaplanalpanama')
