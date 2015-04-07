import json
import time

with open('test.json') as f:
    for line in f:
        test = json.loads(line)
        print test
        print test['name']
        time.sleep(3)

