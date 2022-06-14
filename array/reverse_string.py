class ReverseString:
    def __init__(self, inputString) -> None:
        self.inputString = input

    def reverse(self):
        arr = []
        for i in range(len(self.inputString)-1, -1, -1):
            arr.append(self.inputString[i])
        reversedString = ''.join(arr)
        return reversedString 

       
if __name__=='__main__':
    input  = 'Hi My Name is Sandeep Singh'
    rs = ReverseString(input)
    print(rs.reverse())

