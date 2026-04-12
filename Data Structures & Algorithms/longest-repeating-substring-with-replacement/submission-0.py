class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        start = 0
        max_freq = 0
        ans = 0

        for end in range(len(s)):
            ch = s[end]

            # manual frequency update (no get)
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

            # update max frequency
            if freq[ch] > max_freq:
                max_freq = freq[ch]

            # check validity of window
            while (end - start + 1) - max_freq > k:
                left_char = s[start]
                freq[left_char] -= 1
                start += 1

            ans = max(ans, end - start + 1)

        return ans