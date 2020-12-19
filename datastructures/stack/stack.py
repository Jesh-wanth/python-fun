class Stack:
    """LIFO stack datastructure."""
    def __init__(self):
        self._data = []
    
    def push(self, val):
        self._data.append(val)

    def pop(self):
        return self._data.pop()

    def top(self):
        return self._data[-1]

    def clear(self):
        return self._data.clear()

    def __len__(self):
        return len(self._data)
    
    def empty(self):
        return len(self)==0