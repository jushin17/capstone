import json

with open('test.json') as f:
    for line in f:
        test = json.loads(line)
        print test['name']

