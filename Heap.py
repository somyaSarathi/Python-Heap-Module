from __future__ import annotations

class Heap(object):
    def __init__(self, val: list = list(), __max: bool = False) -> list:
        # error check
        if type(__max) != bool:
            return TypeError( f"Expected an boolean argument, instead got { type(__max) }")

        if type(val) != list:
            return TypeError( f"Expected a list, instead got { type(val) }")

        if not val:
            self.queue = list()
            self.__max = __max
            return

        t = val[0]
        if type(t) != int and type(t) != str:
            raise TypeError( "Expected a list of integers or strings" )

        for x in val:
            if type(x) != type(t):
                raise TypeError( "Expected a list of either (only) intergers or (only) strings" )

        # initializing class instances
        self.queue = val
        self.__max = __max

        if self.__max:
            self.queue.sort(reverse=True)
            return

        self.queue.sort()
        return


    def __add__(self, val: list | 'Heap') -> 'Heap':
        if type(val) == Heap:
            return self.merge(val)
        
        if type(val[0]) != type(self.queue[0]):
            return TypeError( "Expected a list of list of { type( self.queue[0] ) }")

        val = Heap(val, self.__max)
        return self.merge(val)

    
    def __str__(self) -> int:
        if self.__max:
            return f'max-heap{self.queue.__str__()}'
        return f'min-heap{self.queue.__str__()}'


    def __repr__(self) -> int:
        return self.__str__()


    def __len__(self) -> int:
        return self.queue.__len__()


    def __bool__(self) -> bool:
        return bool( self.queue )
    

    def __iter__(self) -> bool:
        return self.queue.__iter__()
    

    def __next__(self) -> bool:
        return self.queue.__next__()


    def __dir__(self) -> list[str]:
        return [ '__add__', '__bool__', '__dir__', '__getitem__', '__init__', '__iter__', '__len__', '__next__', '__repr__', '__str__', '__binSearch', '__merge', 'find', 'merge', 'pop', 'push' ]


    def __getitem__(self, idx) -> any:
        if idx < 0 or idx >= len( self.queue ):
            raise IndexError
        return self.queue[idx]


    def __binSearch(self, val: any) -> int:
        if not self.queue:
            return -1

        l = r = 0
        if self.__max:
            l = len(self.queue) - 1
        else:
            r = len(self.queue) - 1

        def search(val, l, r) -> int:
            if l == r and self.queue[l] != val:
                return -1
            
            mid = (l+r)//2

            if self.queue[mid] == val:
                return mid

            elif self.queue[mid+1] == val:
                return mid+1

            elif self.queue[mid-1] == val:
                return mid-1

            if val > self.queue[mid]:
                return search(val, mid, r)
            
            if val < self.queue[mid]:
                return search(val, l, mid)

        return search(val, l, r)


    def __merge(self, h2: list) -> list:
        i = j = 0
        newArr = list()

        if self.__max:
            while i < len(self.h1) and j < len(h2):
                if self.queue[i] > h2[j]:
                    newArr.append( self.queue[i] )
                    i += 1
                else:
                    newArr.append( h2[j] )
                    j += 1
        
        else:
            while i < len(self.queue) and j < len(h2):
                if self.queue[i] < h2[j]:
                    newArr.append( self.queue[i] )
                    i += 1
                else:
                    newArr.append( h2[j] )
                    j += 1

        while i < len(self.queue):
            newArr.append( self.queue[i] )
            i += 1
        
        while j < len(h2):
            newArr.append( h2[j] )
            j += 1

        return newArr


    def push(self, val: any) -> None:
        '''Appends a new element to the heap'''
        if not self.queue:
            self.queue.append(val)
            return

        if type(self.queue[0]) != type(val):
            raise TypeError( "Expected an element of type { type(self.queue[0]) }, instead got { type(val) }" )

        for i in range( self.queue.__len__() ):
            if self.queue[i] > val:
                self.queue.insert(i, val)
                break
        return


    def pop(self) -> any:
        __return = self.queue[0]
        del self.queue[0]

        return __return


    def merge(self, heap: 'Heap') -> 'Heap':
        if type(heap) != Heap:
            raise TypeError( f"Cannot merge Heap with { type(heap) }" )

        if type(self.queue[0]) != type(heap.queue[0]):
            raise TypeError( f"Expected heaps of same element's type" )

        if self.__max != heap.__max:
            self.queue = self.__merge(heap.queue[::-1])
            return self

        self.queue = self.__merge(heap.queue)
        return self


    def find(self, val: str | int) -> None:
        if type(val) != type( self.heap[0] ):
            raise TypeError( f'Expected a { type( self.heap[0] ) } instead got { type(val) }')
        return self.__binSearch(val)


    def findParentValue(self, val: str | int) -> str | int:
        # error check
        if type(val) != type( self.heap[0] ):
            raise TypeError( f'Expected a { type( self.heap[0] ) } instead got { type(val) }')
        
        if val == self.heap[0]:
            return -1
        
        idx = self.find(val)
        if idx == -1:
            raise ValueError( f'Heap does\'t contain {val}' )
        
        return self.heap[ (idx-1)//2 ]
