def sub_lists (l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists
 
# driver code
l1 = [-2,1,-3,4,-1,2,1,-5,4]
s = sub_lists(l1)
print(s)
# for item in s:
#     total = 0 
#     for ele in item:
#         total = total + ele
#     print(total)