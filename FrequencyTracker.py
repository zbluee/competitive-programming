class FrequencyTracker:

    def __init__(self):
        self.frequency_tracker = defaultdict(int) 
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        if self.freq[self.frequency_tracker[number]] != 0:
            self.freq[self.frequency_tracker[number]] -= 1
        self.frequency_tracker[number] += 1
        self.freq[self.frequency_tracker[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.frequency_tracker[number] > 0:
            if self.freq[self.frequency_tracker[number]] != 0:
                self.freq[self.frequency_tracker[number]] -= 1
            self.frequency_tracker[number] -= 1
            if self.frequency_tracker[number] > 0:
                self.freq[self.frequency_tracker[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
