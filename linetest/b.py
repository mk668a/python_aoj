def time_zone(t):
    t = t.split(':')
    h = int(t[0])
    m = int(t[1])
    s = int(t[2])
    if (17 <= h and 50 <= m and m <= 59) or (18 <= h and h <= 31):
        return "night"
    else:
        return "day"


def room_price(course, t):
    timeZone = time_zone(t)
    if course == "one_drink":
        if timeZone == 'day':
            room_price = 1000
            price_30 = 100
        elif timeZone == 'night':
            room_price = 1500
            price_30 = 400
    elif course == "free_refills":
        if timeZone == 'day':
            room_price = 1500
            price_30 = 200
        elif timeZone == 'night':
            room_price = 2000
            price_30 = 500
    elif course == "alcohol_free_refills":
        if timeZone == 'day':
            room_price = 2500
            price_30 = 300
        elif timeZone == 'night':
            room_price = 4000
            price_30 = 650
    return room_price, price_30


def charge(s, e, price_30):
    s = s.split(':')
    sh = int(s[0])
    sm = int(s[1])
    ss = int(s[2])
    e = e.split(':')
    eh = int(e[0])
    em = int(e[1])
    es = int(e[2])
    hTOm = (eh - sh)*60
    m = em - sm
    s = ss = es
    over = 0
    remain = (hTOm + m) % 30
    if remain >= 10:
        res = (hTOm + m) - remain + 30
    else:
        res = remain
    return res/2*price_30


if __name__ == '__main__':
    li = []
    header = input().split()
    while True:
        i = input().split()
        if i[1] == 'footer':
            footer = i
            break
        else:
            li.append(i)

    timeList = [header[0]]

    time_type, course = header[2], header[3]
    people = []
    num_drink = 0
    num_people = 0
    num_enter = 0
    code = 0

    price = 0
    for l in li:
        # print(l)
        t = l[0]
        timeList.append(t)
        record = l[1]
        if (record == "food" or record == "drink") and num_people < 0:
            code = 1
        else:
            if record == "food":
                price += int(l[2]) * int(l[3])
            elif record == "drink":
                num_drink += int(l[3])
                if course == "one_drink":
                    price += (int(l[2]) * int(l[3]))
                # elif course  == 'free_refills' or course  == 'alcohol_free_refills':
        if record == "enter":
            num_enter += int(l[2])
            for i in range(int(l[2])):
                roomPrice, price_30 = room_price(course, t)
                price += roomPrice
                people.append(t)
            if num_people >= 1000:  # 端末操作エラー
                code = 99
        elif record == "leave":
            num_enter -= int(l[2])
            for i in range(int(l[2])):
                roomPrice, price_30 = room_price(course, people[0])

                price += charge(people[0], t, price_30)

                people = people[1:]
            if num_people < 0:  # 端末操作エラー
                code = 99

    # ワンドリンクエラー
    drink = 0
    if num_drink < num_enter:
        code = 1
        drink = num_enter - num_drink

    timeList.append(footer[0])
    a = sorted(timeList)
    if a != timeList:
        code = 999

    if code == 999:  # 不正な入力エラー
        result = '{"code":999}'
    if code == 99:  # 端末操作エラー
        result = '{"code":99}'
    elif code == 1:  # ワンドリンクエラー
        result = '{"code":1,"price":'+str(price)+',"drink":'+str(drink)+'}'
    elif code == 0:
        result = '{"code":0,"price":'+str(price)+'}'
    print(result)
