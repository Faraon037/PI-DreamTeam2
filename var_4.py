def var4(data,cena):

    name = []
    name_out = []
    for line in data:
        if line.split(",")[0] == "PassengerId":
            continue
        if float(line.split(",")[10]) > float(cena):
            name = [line.split(",")[3] + line.split(",")[4]]
            name_out += name
    return name_out

with open("data.csv") as file:
    data = file.readlines()
print(var4(data,22))