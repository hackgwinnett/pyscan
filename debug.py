def readLines(path):
    f = open(path, "r")
    lines = []
    for x in f:
        l = x.replace("\n", "")
        l = l.strip()
        lines.append(l)
    return lines

def verify(path):
    split = path.split(".")
    if split[1].lower() != "json":
        print("invalid json file, extension is: " + split[1])
        return False
    lines = readLines(path)
    if lines[0] != "{" or lines[len(lines) - 1] != "}":
        print("invalid json structure, starting and ending brackets not present")
        return False
    return True
