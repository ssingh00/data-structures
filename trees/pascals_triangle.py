from typing import List


class Solution:
    def prepare_triangle(self, row_num, path):
        temp = [] 
        if len(path) >= 2:
            temp.append(path[0])
            for i in range(row_num-1):
                temp.append(path[i]+path[i+1])
            temp.append(path[row_num-1])
        elif path == []:
            return [1]
        else:
            return path+path
        return temp
            

    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        path = []
        for i in range(numRows):
            path = self.prepare_triangle(i, path)
            if path is not None:
                res.append(path)
            
        return res

if __name__ == '__main__':
    sl = Solution()
    numRows = 5
    print(sl.generate(numRows))
