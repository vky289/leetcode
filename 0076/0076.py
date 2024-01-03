class Solution:
    def minWindow(self, s: str, t: str) -> str:

        s_freq, t_freq = {}, {}

        found, start, min_sub_string = 0, 0, float('inf')
        res = [-1, -1]

        for c in t:
            s_freq[c] = 0
            t_freq[c] = t_freq.get(c, 0) + 1

        for end in range(len(s)):
            c = s[end]

            if c in t_freq:
                s_freq[c] += 1

                if s_freq[c] == t_freq[c]:
                    found += 1

            while found == len(t_freq):
                if end - start + 1 < min_sub_string:
                    min_sub_string = end - start + 1
                    res = [start, end]

                if s[start] in t_freq:
                    s_freq[s[start]] -= 1
                    if s_freq[s[start]] < t_freq[s[start]]:
                        found -= 1

                start += 1

        return s[res[0]: res[1] + 1] if min_sub_string != float('inf') else ''

