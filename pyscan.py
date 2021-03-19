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
