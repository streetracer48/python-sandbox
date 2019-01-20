import json

#Sample JSON

userJSON = '{"first_name":"jhon", "last_name":"Doe", "age":30}'

#Parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

#Dictionary to json parse format

car ={'make':'Ford', 'model':'Mustang', 'year':2019}

carJSON = json.dumps(car)

print (carJSON)
