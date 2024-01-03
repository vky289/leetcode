class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        def isValid(s):
            if len(s) > 3:
                return False
            return int(s) <= 255 if s[0] != "0" else len(s) == 1


        def backTrack(prevPos, numberOfDots, segments):

            for currPos in range(prevPos + 1, min(len(s)-1, prevPos + 4)):
                segment = s[prevPos + 1 : currPos + 1]
                if isValid(segment):
                    segments.append(segment)
                    if numberOfDots - 1 == 0:
                        segment = s[currPos + 1: len(s)]
                        if isValid(segment):
                            segments.append(segment)
                            result.append('.'.join(segments))
                            segments.pop()
                    else:
                        backTrack(currPos, numberOfDots - 1, segments)
                    segments.pop()

        backTrack(-1, 3, [])
        return result

