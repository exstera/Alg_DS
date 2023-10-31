class DynamicArray:
    def __init__(self):
        self.arr = []

    def get(self, index):
        if 0 <= index < len(self.arr):
            return self.arr[index]
        raise IndexError('Index out of range')

    def set(self, index, value):
        if 0 <= index < len(self.arr):
            self.arr[index] = value
        else:
            raise IndexError('Index out of range')

    def size(self):
        return len(self.arr)

    def append(self, value):
        self.arr.append(value)

    def insert(self, index, value):
        if 0 <= index <= len(self.arr):
            self.arr.insert(index, value)
        else:
            raise IndexError('Index out of range')

    def delete(self, index):
        if 0 <= index < len(self.arr):
            del self.arr[index]
        else:
            raise IndexError('Index out of range')

    def display(self):
        print(self.arr)
