import util

# return all groups:
def get_groups(json_path):
    groups = []
    lines = util.read(json_path)
    for i in range(len(lines)):
        current = lines[i]
        if len(current) > 1 and "{" in current:
            groups.append(current)
    groups = util.clean(groups)
    return groups

# return all individual properties:
def get_indiv(json_path):
    indiv = []
    indices = []
    result = []
    lines = util.read(json_path)

    for i in range(len(lines)):
        current = lines[i]
        if len(current) > 1 and "{" not in current:
            indiv.append(current)
            indices.append(i)
    
    for i in range(len(indiv)):
        if not util.in_group(json_path, indices[i]):
            result.append(indiv[i])

    for i in range(len(result)):
        result[i] = result[i].replace(",", "")
        result[i] = result[i].replace("\"", "")
        result[i] = result[i].split(": ")[0]
        result[i]
        if result[i] == "{" or result[i] == "}":
            result.pop(i)
    
    return result

# read an individual property:
def read_indiv(json_path, indiv_name):

    lines = util.read(json_path)
    for i in range(len(lines)):
        line = lines[i]
        if not util.in_group(json_path, i) and line != "{" and line != "}":
            name = line.split(": ")[0]
            name = name.replace("\"", "")
            if name == indiv_name:
                val = line.split(": ")[1]
                val = val.replace("\"", "")
                val = val.replace(",", "")
                return val

    return "error: no value found"

# return a group property:
def read_group(json_path, group, name):
    lines = util.read(json_path)
    lines = util.clean(lines)
    for i in range(len(lines)):
        if group in lines[i]:
            raw = read_group_helper(lines, i, name)
            raw = str.replace(raw, ",", "")
            val = raw.split(" ")[1]
            return val

    return "error: no value found"

# helper group property function:
def read_group_helper(lines, n, name):
    i = n
    while (i < len(lines)):
        if name in lines[i]:
            return lines[i]
        i+=1
