# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    file_dict = {}

    for file in files:
        temp = file
        file_name = ""
        while temp[-1] != "/":
            file_name = temp[-1] + file_name
            temp = temp[:-1]
        if file_name not in file_dict:
            # print(f"not in dict adding {file_name}")   
            file_dict[file_name] = {}
            file_dict[file_name][file] = 0
        else:
            # print(f"already in dict {file_name}")   
            file_dict[file_name][file] = 0
        file_name = ""
    q = []
    for query in queries:
        if query in file_dict:
            for key in file_dict[query].keys():
                q.append(key)
    return q


    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        'home/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
