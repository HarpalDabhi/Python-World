import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

y='{45,45,78,15,2,60}'


# convert into JSON:
z = json.dumps(y)

# the result is a JSON string:
print(z)