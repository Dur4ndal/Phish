import requests

file = open('output.json','rb')

test = requests.post('https://localhost:3333/api/groups/', file, verify=False, headers={'Authorization': 'b9df0908f9fb99e4397a32d96cf2348413fd7e7b6b2600bf8e26a93fdcf78c29'})
file.close()
print(test.text)
