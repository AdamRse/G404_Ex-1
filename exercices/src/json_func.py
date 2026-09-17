import json

# url = "https://jsonplaceholder.typicode.com/todos/1"

# with urllib.request.urlopen(url) as response:
#      body_json = response.read()

# body_dict = json.loads(body_json)
# user_id = body_dict['userId']
fileJson=""
with open('data/listeDep.json') as f:
    fileJson = json.load(f)
print(fileJson["publisher"])
