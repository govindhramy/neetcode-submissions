from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self._store = defaultdict(SortedDict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._store[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._store:
            return ""
        
        timestamps = self._store[key]
        idx = timestamps.bisect_right(timestamp)-1

        if idx >= 0:
            return timestamps[timestamps.iloc[idx]]
        return ""

        
