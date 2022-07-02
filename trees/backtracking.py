from typing import List
class AllSubset:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtracking(nums,[])
        return self.res

    def backtracking(self,nums,path):
        if  path not in self.res:
            self.res.append(path)
            
        for i in range(len(nums)):
            self.backtracking(nums[i+1:],path+[nums[i]])

if __name__ == '__main__':
    als = AllSubset()
    nums = [1,2,3]
    res= als.subsets(nums)
    print(als.count)
    print(res)

