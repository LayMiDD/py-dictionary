class Dictionary:
    def __init__(self, size: int = 8):
        self.size = size
        self.slots = [[] for _ in range(self.size)]
    
    def _get_index(self, key):
        return abs(hash(key)) % self.size
    
    def __setitem__(self, key, value):
        index = self._get_index(key)
        for pair in self.slots[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.slots[index].append([key, value])

    def __getitem__(self, key):
        index = self._get_index(key)
        for pair in self.slots[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError
    
    def __len__(self):
        return sum(len(slot) for slot in self.slots)
    
    