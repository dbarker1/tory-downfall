f_csv = open("tsv-data.txt")
csv_data = f_csv.read()

keys = []
i = 0
data_arr = []

for line in csv_data.split("\n"):
    if (i == 0):
        for key in line.split("\t"):
            if (key == "\ufeffConstituency"):
                keys.append("Constituency")
            else:
                keys.append(key)
        i += 1
        continue

    j=0
    obj = {}
    for val in line.split("\t"):
        try:
            if (keys[j] == "Majority (%)"):
                obj[keys[j]] = float(val.replace("%", ""))
            else:
                obj[keys[j]] = val
        except:
            print("Error getting " + line)
        
        j += 1

    data_arr.append(obj)
    i += 1

print(data_arr)