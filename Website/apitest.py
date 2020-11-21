import requests,json;

"""In this file, we are working on get request of Json. The data is outputted to views.py file"""

resp = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeId/440?format=json')
data = resp.json()

Model_ID = []
Make_ID = []

# print(data["Results"][1]["Make_ID"])

for i in range(0,14):
    x = data["Results"][i]["Make_ID"]
    y = data["Results"][i]["Model_ID"]
    Model_ID.append(y)
    Make_ID.append(x)

# print(Model_ID)
# print(Make_ID)