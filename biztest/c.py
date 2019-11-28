import sys
import urllib.request
import urllib.parse
import json


def getAPI(q):
    # url = "http://challenge-server.code-check.io/"
    # params = {
    #     'q': q[0],
    # }

    # req = urllib.request.Request('{}?{}'.format(
    #     url, urllib.parse.urlencode(params)))
    # with urllib.request.urlopen(req) as res:
    #     body = res.read()
    #     print(body)

    params = urllib.parse.urlencode({'q': q[0]})
    url = "http://challenge-server.code-check.io?%s" % params
    with urllib.request.urlopen(url) as f:
        print(f.read().decode('utf-8'))


def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.
    getAPI(argv)


if __name__ == '__main__':
    main(sys.argv[1:])
