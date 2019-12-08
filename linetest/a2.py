import re


def callA(k, s):
    # for i in range(k):
    patternSSS = re.compile('SSS')
    SSS = patternSSS.search(s)

    patternSS = re.compile('SS')
    SS = patternSS.search(s)

    doubleS = re.compile('S\.S')
    dS = doubleS.search(s)

    rightS = re.compile('\.S')
    rS = rightS.search(s)

    leftS = re.compile('S\.')
    lS = leftS.search(s)

    if SSS:
        SSS = SSS.group()
        s = patternSSS.sub('...', s, 1)
    elif dS:
        dS = dS.group()
        s = doubleS.sub('...', s, 1)
    elif SS:
        SS = SS.group()
        s = patternSS.sub('..', s, 1)
    elif rS:
        rS = rS.group()
        s = rightS.sub('..', s, 1)
    elif lS:
        lS = lS.group()
        s = leftS.sub('..', s, 1)
    return s


def callB(k, s):
    # for i in range(k):
    patternSSS = re.compile('SSS')
    SSS = patternSSS.search(s)

    patternSS = re.compile('SS')
    SS = patternSS.search(s)

    doubleS = re.compile('S\.S')
    dS = doubleS.search(s)

    rightS = re.compile('\.S')
    rS = rightS.search(s)

    leftS = re.compile('S\.')
    lS = leftS.search(s)

    if dS:
        dS = dS.group()
        s = doubleS.sub('...', s, 1)
    elif SSS:
        SSS = SSS.group()
        s = patternSSS.sub('...', s, 1)
    elif SS:
        SS = SS.group()
        s = patternSS.sub('..', s, 1)
    elif rS:
        rS = rS.group()
        s = rightS.sub('..', s, 1)
    elif lS:
        lS = lS.group()
        s = leftS.sub('..', s, 1)
        # print(i, s)
    return s


if __name__ == '__main__':
    n, k = (int(x)for x in input().split())
    s = input()
    res = []
    li = [s, s]
    for i in range(k):
        for l in li:
            a = callA(k, l)
            b = callB(k, l)
            li.append(a)
            li.append(b)
            res.append(a.count('.'))
            res.append(b.count('.'))
        li = []
        li = [a, b]

    # a = callA(k, s)
    # b = callB(k, s)
    # if a.count('.') > b.count('.'):
    #     result = a.count('.')
    # else:
    #     result = b.count('.')
    print(min(li))
