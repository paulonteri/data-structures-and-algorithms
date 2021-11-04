"""
Design Underground System: Leetcode 1396

Implement the class UndergroundSystem that supports three methods:
    1. checkIn(int id, string stationName, int t)
        A customer with id card equal to id, gets in the station stationName at time t.
        A customer can only be checked into one place at a time.
    2. checkOut(int id, string stationName, int t)
        A customer with id card equal to id, gets out from the station stationName at time t.
    3. getAverageTime(string startStation, string endStation) 
        Returns the average time to travel between the startStation and the endStation.
        The average time is computed from all the previous traveling from startStation to endStation that happened
        directly.
        Call to getAverageTime is always valid.
You can assume all calls to checkIn and checkOut methods are consistent. 
That is, if a customer gets in at time t1 at some station, then it gets out at time t2 with t2 > t1. 
All events happen in chronological order.
"""


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)x


class UndergroundSystem:

    def __init__(self):
        self.checkin_details = {}
        self.route_total_time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # save journey start details for each passenger
        # save cutomer checkin details
        self.checkin_details[id] = {
            "station": stationName,
            "time": t
        }

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin = self.checkin_details[id]
        # time taken = end time - start time
        time_taken = t - checkin["time"]

        # path = start station + end station
        path = checkin["station"] + stationName

        # increase total time and count
        if path in self.route_total_time:
            prev_total = self.route_total_time[path]

            self.route_total_time[path] = {
                "total": prev_total["total"] + time_taken,
                "count": prev_total["count"] + 1
            }

        # create entry in route_total_time: record total time and the count as 1
        else:
            self.route_total_time[path] = {
                "total": time_taken,
                "count": 1
            }

        # end customer journey
        self.checkin_details.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        path = startStation + endStation
        # calculate average
        return self.route_total_time[path]["total"] / self.route_total_time[path]["count"]


"""
Input:
    ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime",
    "getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
    [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],
    ["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],
    ["Leyton","Waterloo"]]
Output:
    [null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]
"""
