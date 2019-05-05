import collections.abc


class SortedList(collections.abc.Sequence):
    def __init__(self, sequence = None, key=None):
        if key is None:
            self.key = lambda a:a
        else:
            self.key = key
        if sequence is None:
            self._list = []
        elif isinstance(sequence, SortedList) and sequence.key == self.key:
            self._list = sequence._list
        else:
            self._list = sorted(list(sequence), key = self.key)

    def __getitem__(self, item):
        return self._list[item]

    def __len__(self):
        return len(self._list)

    def add(self, item):
        index = self._find_index(item)
        self._list.insert(index, item)

    def clear(self):
        self._list = []

    def pop(self, i=-1):
        return self._list.pop(i)

    def extend(self, sequence):
        for i in sequence:
            self.add(i)

    def _find_index(self, item):
        l = 0
        r = len(self._list) - 1
        keyItem = self.key(item)
        while l <= r:
            mid = (l + r) //2

            if self.key(self._list[mid]) < keyItem:
                l = mid + 1
            else:
                r = mid -1
        return l

    def count(self, x):
        count = 0
        index = self._find_index(x)
        lenght = len(self._list)
        while index > lenght and self._list[index] == x:
            count += 1
            index += 1
        return count

    def remove(self, x):
        index = self._find_index(x)
        if index < len(self._list) and self._list[index] == x:
            del self._list[index]

    def removeAll(self, x):
        index = self._find_index(x)
        lenght = len(self._list)
        while index < lenght and self._list[index] == x:
            del self._list[index]

    def __str__(self):
        # return f"{self._list} \t"
        return str(self._list)


a = (1, 1)
list = SortedList(a)

print(list._find_index(2))
list.add(2)
list.add(10)
list.add(-1)
list.add(3)
print(list)

list.removeAll(1)
print(list)