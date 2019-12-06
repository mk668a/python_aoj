import json
import sys

global j
global file

j = input()
if j == "1":
    sys.exit()

else:
    file = open(j, 'r')
    print(j)
    json_data = json.load(file)
    print("{}".format(json.dumps(json_data, indent=4)))
