import sys


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    # input.inの値を数字に変換して格納するための配列
    numList = []

    for i in range(0, len(lines)):
        # 最初が0以外の値を追加
        v = lines[i]
        if(v and v[0] != "0"):
            numList.append(int(v))
    # 最小値を出力
    if(len(numList) >= 100):
        numList = numList[0:100]
    if(numList):
        print(min(numList))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
