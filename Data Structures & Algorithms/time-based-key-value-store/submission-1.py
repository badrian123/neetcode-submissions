class TimeMap:
    #Store multiple values for the same key at different time stamps.
        #like a dictionary:
            #key -> key
            #value -> [value, timestamp]

    def __init__(self):
        #This one is easy. Just create a dictionary
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #This one requires me to create the key and store it's values
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        #This one requires me to do a bit of a few things.
        #I need to get the values from the dictionary based on key.
        #Then I need to find what's being requested in the returned data.

        res = ""
        values = self.storage.get(key, [])
        #Right? I am going to get the values like this. yea.

        #Now I need to search for what's being requested.
        l, r = 0, len(values)-1
        while l <= r:
            m = (l + r) // 2

            #ok. So I have my binary search done.
            #I just need to check the values until I find what is being requested.
            if values[m][1] <= timestamp:
                res = values[m][0] #result equal to value
                l = m + 1
            else:
                r = m - 1
        return res









