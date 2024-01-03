class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        string_len = len(s)
        char_freq = {}
        max_char_freq = 0
        start = 0
        len_of_max_substring = 0


        for end in range(string_len):

            char_freq[s[end]] = char_freq.get(s[end], 0) + 1

            max_char_freq = max(max_char_freq, char_freq[s[end]])

            if end + 1 - start - max_char_freq > k:
                char_freq[s[start]] -= 1
                start += 1

            len_of_max_substring = max(len_of_max_substring, end + 1 - start)

        return len_of_max_substring

