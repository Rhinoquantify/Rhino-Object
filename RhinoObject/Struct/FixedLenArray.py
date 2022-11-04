class FixedLenArray:
    def __init__(self, size=32):
        self._is_empty = True
        self._size = size
        self._exist_size = 0
        self._items = [None] * size

    def __len__(self):
        return self._size

    def insert_head(self, value):
        # 倒序插入
        if self._exist_size < self._size:
            self._exist_size += 1
        self._is_empty = False
        for i in range(self._size, 1, -1):
            self._items[i - 1] = self._items[i - 2]
        self._items[0] = value

    def insert_end(self, value):
        self._is_empty = False
        if self._exist_size < self._size:
            self._items[self._exist_size] = value
            self._exist_size += 1
        else:
            for i in range(0, self._exist_size - 1):
                self._items[i] = self._items[i + 1]

    def get_index(self, index):
        if index > self._size - 1:
            return None
        else:
            return self._items[index]

    def get_exist(self):
        return self._items[:self._exist_size]

    def get_all(self):
        return self._items

    def clear(self):
        self._is_empty = False
        self._items = [None] * self._size

    def count(self, value):
        _count = 0
        for item in self._items:
            if item == value or item is value:
                _count += 1
        return _count

    def is_exist(self, value):
        for item in self._items:
            if item == value or item is value:
                return True
        return False

    def get_size(self):
        return self._size

    def get_exist_size(self):
        return self._exist_size
