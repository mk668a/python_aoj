import sys
import re
from collections import Counter

file = open(sys.argv[1], encoding="utf-16")
readfile = re.split('[ \n,.]', file.read())
file.close()
c = Counter(readfile).most_common()
for i in range(1, int(sys.argv[2]) + 1):
    print(c[i][0], c[i][1])
