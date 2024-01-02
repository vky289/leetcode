class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        start, end = 0, len(people)-1
        people.sort()
        boat = 0

        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            end -=1
            boat +=1

        return boat