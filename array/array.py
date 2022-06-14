class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}
        
    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length+=1
        return self.length

    def pop(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return lastItem

    
    def delete(self, index):
        item = self.data[index]
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length-=1
        return item


if __name__ == "__main__":
    arr = MyArray()
    arr.push(3)
    arr.push('hi')
    arr.push(34)
    arr.push(20)
    arr.push('hey')
    arr.push('welcome')
    print("Before Deletion", arr)
    arr.delete(3)
    print("After Deletion", arr)