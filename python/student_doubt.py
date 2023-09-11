#Usage of JSON.LOADS

import json

x = {"name":"abc","age":23}

print(x['name'])


y = '{"name":"abc","age":23}'

data = json.loads(y)

print(data['name'])
