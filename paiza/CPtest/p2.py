import urllib.request
import urllib.parse
import json


def getPoint(bet, points):
    global total, win, lose
    url = 'https://tanaka-server.herokuapp.com/'
    data = {
        'bet': bet,
        'points': points
    }
    data = urllib.parse.urlencode(data).encode("utf-8")
    with urllib.request.urlopen(url, data=data) as res:
        endpoint = json.loads(res.read().decode("utf-8"))
        dice = endpoint['dice']
        result = endpoint['result']
        res_points = endpoint['points']
        print("Dice: " + str(dice))
        print("Result: " + str(result))
        print("Points: " + str(res_points) + "\n")
        if result == bet:
            win += 1
            total += points
        else:
            lose += 1
            total -= points


total = 20
win = 0
lose = 0
for i in range(3):
    print("Total: " + str(total))
    if total == 0:
        print("You can't bet because your points are 0\n")
        break
    bet = 0
    while bet != 'odd' and bet != 'even':
        print("Input your bet(odd, even) >> ", end='')
        bet = input()
    points = -1
    while points < 0 or points > total:
        print("Input your bet points(0 - " + str(total) + ") >> ", end='')
        points = int(input())
    getPoint(bet, points)

print("#### finish ####")
print("Win: " + str(win))
print("Lose: " + str(lose))
print("Total points " + str(total))
