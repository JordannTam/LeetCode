class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append([value, timestamp])
        self.d[key] = sorted(self.d[key], key=lambda x: x[1])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        ls = self.d[key]
        n = len(ls) - 1
        l = 0
        r = n

        while(l <= r):
            mid = (l + r) // 2
            if timestamp == ls[mid][1]:
                return ls[mid][0]
            elif ls[mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        if l > n:
            l = n
        if ls[l][1] > timestamp:
            if l == 0:
                return ""
            else:
                return ls[l - 1][0]
        else:
            return ls[l][0]


if __name__ == "__main__":
    result = []
    obj = TimeMap()
    result.append(obj.set("love","high",10))
    result.append(obj.set("love","low",20))
    result.append(obj.get("love",5))
    result.append(obj.get("love",10))
    result.append(obj.get("love",15))
    result.append(obj.get("love",20))
    result.append(obj.get("love",25))
    print(result)
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

