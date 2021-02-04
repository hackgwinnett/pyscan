path = "debug.json"

f = open(path, "r")
lines = []
for x in f:
    l = x.replace("\n", "")
    l = l.strip()
    lines.append(l)

for x in lines:
    if "{" not in x and ":" in x:
        x = x.replace("\"", "")
        arr = x.split(":")
        arr[0] = arr[0].strip()
        arr[1] = arr[1].strip()
        print("field: " + str(arr[0]) + ", val: " + str(arr[1]))
