class MergeTwoSortedArray:
    def __init__(self,array1,array2) -> None:
        self.array1 = array1
        self.array2 = array2

    def merge(self):
        mergedArray = []
        if len(self.array1) == 0:
            return self.array2
        if len(self.array2) == 0:
            return self.array1
        i = 0
        j = 0
        while i < len(self.array1) and j< len(self.array2):
            if self.array1[i] <= self.array2[j]:
                mergedArray.append(self.array1[i])
                i+=1
            elif self.array2[j] <= self.array1[i]:
                mergedArray.append(self.array2[j])
                j+=1
        return mergedArray+self.array1[i:]+self.array2[j:]

if __name__=="__main__":
    array1 = [1,3,4,6,20]
    array2 = [2,3,4,5,6,9,11,76]
    mtsa = MergeTwoSortedArray(array1,array2)
    print(mtsa.merge())

    