class TimeMap:
    #Create a data structure
        #That stores multiple values for same key
            #At different time stamps and
        #Can retrieve the key's value at a certain timestamp.

    def __init__(self):
        #So creating a dictionary
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #Adding to the dictionary.
            #Having a condition where key doesn't exist so one is created for it.
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, []) #get the values from dict or empty array
        
        #Binary search through values
        l, r = 0, len(values)-1
        while l <= r:
            m = (l + r) // 2
            #Checking for our requested timestamp
            if values[m][1] <= timestamp:
                #We found it.
                res = values[m][0]
                #interesting how we adjust left position
                #Probably to cause loop to stop.
                l = m + 1
            else:
                r = m -1
        return res
