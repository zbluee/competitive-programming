class UndergroundSystem:

    def __init__(self):
        self.checkInData = {}
        self.dest = defaultdict(lambda : [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInData[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, start_time = self.checkInData[id]
        self.dest[(startStation, stationName)][0] += t - start_time
        self.dest[(startStation, stationName)][1] += 1
        del self.checkInData[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_travel_time, count_travels = self.dest[(startStation, endStation)]
        return total_travel_time / count_travels
            
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
