class Geometric:
    def __init__(self, start: float, rate: float):
        self.start = start
        self.rate = rate

    def __getitem__(self, idx: int):
        return self.start*self.rate**idx
    
    def __iter__(self):
        return GeometricIterator(self, self.start, self.rate)


class GeometricIterator:
    def __init__(self, start: float, rate: float):
        if rate == 0:
            raise ValueError('rate cannot be 0')
        self.value = start/rate
        self.rate = rate

    def __iter__(self):
        return self

    def __next__(self):
        self.value *= self.rate
        return self.value
