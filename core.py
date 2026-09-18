import ctypes

class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0

        # create a C type arrary with size = self.size
        self.A = self.__make_array(self.size)

    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'              #[:-1] removes the last ,
            

    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError: Index out of range'


    def __len__(self):
        return self.n

    def append(self, item):
        if self.n == self.size: # check if array is empty or not
            # resize
            self.__resize(self.size*2)
        
        # append
        self.A[self.n] = item
        self.n = self.n + 1

    def pop(self):
        if self.n == 0:
            return 'Empty list'

        print(self.A[self.n-1])
        self.n = self.n -1


    def __resize(self, new_capacity):
        # create a new array with new capacity
        B = self.__make_array(new_capacity) # B is an array double the size of A
        self.size = new_capacity

        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]

        # reassign A because all the logic are written in A.
        self.A = B

    def __make_array(self, capacity):
        # this creates c type static & referential array with size capacity
        return (capacity*ctypes.py_object)()

L = MeraList()

# test append
L.append('Hello')
L.append(2)
L.append(True)

# test print
print(L)

# test indexing
print(L[0])
print(L[5]) 

print(type(L), len(L))