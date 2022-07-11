
def query(cmd, value, file_list):
    if cmd == "filter":
        result = filter(lambda row: value in row, file_list)
        return result
    if cmd == "map":
        result = [row.split()[int(value)] for row in file_list]
        return result
    if cmd == "unique":
        result = list(set(file_list))
        return result
    if cmd == "sort":
        reverse = value == "desc"
        result = sorted(file_list, reverse=reverse)
        return result
    if cmd == "limit":
        result = list(file_list)[:int(value)]
        return result
