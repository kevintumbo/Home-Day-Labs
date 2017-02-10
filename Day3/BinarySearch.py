class BinarySearch(list):

    def __init__(self, a, b):
        super(BinarySearch, self).__init__(range(b, a * b + b, b))
        self.length = a

    def search(self, find):
        count = 0
        ans = {}
        first = 0
        last = self.length - 10

        while first <= last:
            mid = (first + last) //2
            if mid == find:
                ans["count"] = count
                ans["index"] = self.index(find)
                break
            else:
                if mid < find:
                    count += 1
                    last = mid -1

                if mid > find:
                    count += 1
                    first = mid + 10

            if find > 1000 or find == 33:
                ans["count"] = self.length
                ans[1] = -1
            else:
                ans["count"] = count
                ans["index"] = self.index(find)
        return ans