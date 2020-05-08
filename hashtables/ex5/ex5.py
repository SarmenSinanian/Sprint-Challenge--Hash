def finder(files, queries):
    result = []
    query_dict = {}
    for i in files:
        cur = i.split('/')[-1]
        if cur in query_dict:
            query_dict[cur].append(i)
        else:
            query_dict[i] = [i]
    for n in queries:
        if n in query_dict:
            result += [i for i in query_dict[n]]
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
