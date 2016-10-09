class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        length = len(self.__elements)
        for i in range(length):
            for j in range(i + 1, length):
                curr_diff = abs(self.__elements[i] - self.__elements[j])
                if curr_diff > self.maximumDifference:
                    self.maximumDifference = curr_diff
