#coding:utf-8

class Search:
    def __init__(self):
        pass

    def BinarySearch(self, target, numlist):
        low == 0
        high == len(numlist) -1

        while low <= high:
            middle = (low + high) / 2
            if target == numlist[middle]:
                return True
            elif target > numlist[middle]:
                low = middle + 1
            elif target < numlist[middle]:
                high = middle - 1
        return False


class SearchTemplateMethod:
    def __init__(self, category, num ):
        pass

    def Search:
        pass
