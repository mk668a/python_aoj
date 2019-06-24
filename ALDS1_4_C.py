l = {}
for i in range(int(input())):
    a = input()
    if a[0] == 'i':
        l[a[7:]]=0
    else:
        print('yes' if a[5:] in l else 'no')
