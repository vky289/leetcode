from heapq import heappush, heappop

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        if startFuel >= target:
            return 0
        i, n, stops = 0, len(stations), 0
        heap = []
        while startFuel < target:
            if i<n and stations[i][0] <= startFuel:
                heappush(heap, (-stations[i][1], i))
                i += 1
            elif not heap:
                return -1
            else:
                nexFuel, iter = heappop(heap)
                startFuel += -nexFuel
                stops += 1

        return stops

