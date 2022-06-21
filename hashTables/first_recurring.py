def find_first_recurring(arr):
    dictionary = dict()
    for item in arr:
        if item in dictionary:
            return item
        else:
            dictionary[item] = True

        print(dictionary)
    return None


arr = [2,1,4,2,6,5,1,4]
out = find_first_recurring(arr)
print(out)