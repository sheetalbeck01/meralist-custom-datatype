import ctypes

class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0

        # create a C type arrary with size = self.size
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n


    def __make_array(self, capacity):
        # this creates c type static & referential array with size capacity
        return (capacity*ctypes.py_object)()

L = MeraList()

print(type(L), len(L))