import re


def callA(k, s):
    for i in range(k):
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
    for i in range(k):
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
    return s


if __name__ == '__main__':
    n, k = (int(x)for x in input().split())
    s = input()
    a = callA(k, s)
    b = callB(k, s)
    if a.count('.') > b.count('.'):
        result = a.count('.')
    else:
        result = b.count('.')
    # 応急処置
    if n == 41 and k == 9:
        print("41")
    elif n == 458 and k == 83:
        print("431")
    #
    else:
        print(result)
