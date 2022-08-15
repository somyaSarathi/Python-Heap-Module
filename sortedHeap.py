from __future__ import annotations

class sortedHeap(object):
    def __init__(self, val: list = list(), __max: bool = False) -> list:
        # error check
        if type(__max) != bool:
            return TypeError( f"Expected an boolean argument, instead got {type(__max)}")

        if type(val) != list:
            return TypeError( f"Expected an list argument, instead got {type(val)}")

        t = val[0]
        if type(t) != int and type(t) != str:
            raise TypeError( "Expected a list of integers or strings" )

        for x in val:
            if type(x) != type(t):
                raise TypeError( "Expected a list of either only intergers or only strings" )

        # initializing class instances
        self.heap = val
        self.__max = __max

        if self.__max:
            self.heap.sort(reverse=True)
            return

        self.heap.sort()
        return


    def __add__(self, val: list | 'sortedHeap') -> 'sortedHeap':
        if type(val) == sortedHeap:
            return self.merge(val)
        
        if type(val[0]) != type(self.heap[0]):
            return TypeError( "Expected a list of list of {type(self.heap[0])}")

        val = sortedHeap(val, self.__max)
        return self.merge(val)

    
    def __str__(self) -> int:
        if self.__max:
            return f'max-heap{self.heap.__str__()}'
        return f'min-heap{self.heap.__str__()}'


    def __repr__(self) -> int:
        return self.__str__()


    def __len__(self) -> int:
        return self.heap.__len__()


    def __bool__(self) -> bool:
        return bool( self.heap )
    

    def __iter__(self) -> bool:
        return self.heap.__iter__()
    

    def __next__(self) -> bool:
        return self.heap.__next__()


    def __dir__(self) -> list[str]:
        return [ '__add__', '__bool__', '__dir__', '__getitem__', '__init__', '__iter__', '__len__', '__next__', '__repr__', '__str__', '__binSearch', '__merge', 'find', 'merge', 'pop', 'push' ]


    def __getitem__(self, idx) -> any:
        if idx < 0 or idx >= len( self.heap ):
            raise IndexError
        return self.heap[idx]


    def __binSearch(self, val: any) -> int:
        if not self.heap:
            return -1

        l = r = 0
        if self.__max:
            l = len(self.heap) - 1
        else:
            r = len(self.heap) - 1

        def search(val, l, r) -> int:
            if l == r and self.heap[l] != val:
                return -1
            
            mid = (l+r)//2

            if self.heap[mid] == val:
                return mid

            elif self.heap[mid+1] == val:
                return mid+1

            elif self.heap[mid-1] == val:
                return mid-1

            if val > self.heap[mid]:
                return search(val, mid, r)
            
            if val < self.heap[mid]:
                return search(val, l, mid)

        return search(val, l, r)


    def __merge(self, h2: list) -> list:
        i = j = 0
        newArr = list()

        if self.__max:
            while i < len(self.h1) and j < len(h2):
                if self.heap[i] > h2[j]:
                    newArr.append( self.heap[i] )
                    i += 1
                else:
                    newArr.append( h2[j] )
                    j += 1
        
        else:
            while i < len(self.heap) and j < len(h2):
                if self.heap[i] < h2[j]:
                    newArr.append( self.heap[i] )
                    i += 1
                else:
                    newArr.append( h2[j] )
                    j += 1

        while i < len(self.heap):
            newArr.append( self.heap[i] )
            i += 1
        
        while j < len(h2):
            newArr.append( h2[j] )
            j += 1

        return newArr


    def push(self, val: any) -> None:
        if not self.heap:
            self.heap.append(val)
            return

        for i in range( self.heap.__len__() ):
            if self.heap[i] > val:
                self.heap.insert(i, val)
                break
        return


    def pop(self) -> any:
        __return = self.heap[0]
        del self.heap[0]

        return __return


    def merge(self, heap: 'sortedHeap') -> 'sortedHeap':
        if type(heap) != sortedHeap:
            return TypeError( f"Cannot merge Heap with {type(heap)}" )

        if type(self.heap[0]) != type(heap.heap[0]):
            return TypeError( f"Expected heaps of same element's type" )

        if self.__max != heap.__max:
            self.heap = self.__merge(heap.heap[::-1])
            return self

        self.heap = self.__merge(heap.heap)
        return self


    def find(self, val: any) -> None:
        return self.__binSearch(val)
