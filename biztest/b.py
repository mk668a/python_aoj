import sys


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    # 数字のリスト
    numList = []
    # 数字に対応した文字列のリスト
    strList = []

    # 空白で区切る
    lines = lines[0].split()

    # ターゲットの値
    target = lines[len(lines)-1]

    # 数字と文字を分けてそれぞれ配列に格納
    lines = lines[0:len(lines)-1]
    for i in range(0, len(lines)):
        v = lines[i].split(":")
        num = int(v[0])
        string = v[1]
        if(0 < num and num <= 20 and 0 < len(string) and len(string) <= 11):
            numList.append(v[0])
            strList.append(v[1])

    res = ""
    for i in range(len(numList)):
        if(int(target) % int(numList[i]) == 0):
            res += strList[i]

    if(res == ""):
        print(target)
    else:
        print(res)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
