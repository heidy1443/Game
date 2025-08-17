class Jar:
    def __init__(self,size=0, capacity=12):
        self.capacity=capacity
        self.size=size

    def __str__(self):
            return "🍪" * self.size
        
    def deposit(self, n):
        if self.size+n >self.capacity:
            raise ValueError("The Jar is full.")
        self.size+=n
        
        
    def withdraw(self, n):
        if self.size-n<0:
            raise ValueError("Not enough cookie in the Jar.")
        self.size-=n
        
        

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self,capacity):
        if capacity <0:
            raise ValueError("Invalid capacity")
        self._capacity=capacity
        
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,size):
        if size<0 or size>self.capacity:
            raise ValueError("Invalid capacity")
        self._size=size


        