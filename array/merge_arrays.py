from typing import List
class MergeTwoSortedArray:
    def __init__(self,array1,array2) -> None:
        self.array1 = array1
        self.array2 = array2
        self.m=m
        self.n=n

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

def mergeinplace(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """ 
    Do not return anything, modify nums1 in-place instead.
    """
        # Initialize nums1's index
    i = m - 1
    # Initialize nums2's index
    j = n - 1
    # Initialize a variable k to store the last index of the 1st array...
    k = m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1


if __name__=="__main__":
    array1 = [1,3,4,6,20]
    array2 = [2,3,4,5,6,9,11,76]
    mtsa = MergeTwoSortedArray(array1,array2)
    print(mtsa.merge())

    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 3
    mergeinplace(nums1, m, nums2, n)
    nums1 = [1]
    m = 1 
    nums2 = []
    n = 0
    mergeinplace(nums1, m, nums2, n)




    