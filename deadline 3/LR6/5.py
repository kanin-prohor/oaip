class SmartList(list):
    def __getitem__(self, index):
        if isinstance(index, slice):
            return super().__getitem__(index)
        if index < 0:
            if abs(index) > len(self):
                raise IndexError("Индекс за пределами списка")
            return super().__getitem__(-index - 1)
        return super().__getitem__(index)