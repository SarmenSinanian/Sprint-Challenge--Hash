def has_negatives(a):
    negs = []
    table = {}
    # table = {len(a) * [None]}
    for i in a:
        table[i] = None
    for i in a:
        if i > 0:
            if i * -1 in table:
                negs.append(i)
    return negs


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))


# def myhash(n):
#     if abs(a) == abs(b):
#         # add a to b's hash
#     return n


# a = [-1,-2,1,2,3,4,-4]
# b = len(a)
# table = {}
# for i in a:
#     table[i] = None
# # table = {len(a) * [None]}
# print(table)