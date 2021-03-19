def read(json_path):
    f = open(json_path, "r")
    lines = []
    for x in f:
        l = x.replace("\n", "")
        l = l.strip()
        lines.append(l)
    return lines

def clean(arr):
    for j in range(len(arr)):
        arr[j] = arr[j].replace("{", "")
        arr[j] = arr[j].replace("\"", "")
        arr[j] = arr[j].replace(":", "")
        arr[j] = arr[j].strip()
    return arr



def in_group(json_path, line):

    # creates 2d array of boundaries, each array being a container holding starting and ending group line indexes:
    lines = read(json_path)
    bounds_list = []

    for i in range(len(lines)):
        current = lines[i]
        if len(current) > 1 and "{" in current:
            bounds = [i]

            pos = i + 1
            while pos < len(lines):
                end = lines[pos]
                if end == "}" or end == "},":
                    bounds.append(pos)
                    break
                pos += 1
            
            bounds_list.append(bounds)

    # checks if the passed index is within the starting or ending bounds of all the bounds in the 2d array:
    for i in range(len(bounds_list)):
        current_bound = bounds_list[i]
        min = current_bound[0]
        max = current_bound[1]
        if line > min and line < max:
            return True

    return False
