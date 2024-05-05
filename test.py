import json

with open("data/map.json","r") as file:
    data = json.load(file)
    world = data["theworld"]["world"]
    events = data["theworld"]["events"]
    spawn = data["theworld"]["spawn"]

def getworld(spawn):
    warr = []
    for i in range(spawn[0],spawn[0]+59):
        arr = []
        arr = world[i][ spawn[1]:spawn[1]+59 ]
        warr.append(arr)

    return warr

print(len(world),len(world[0]))

for i in range(0,40):
    for j in range(0,40):
        a = getworld([i,j])
        print(len(a),len(a[0]))
