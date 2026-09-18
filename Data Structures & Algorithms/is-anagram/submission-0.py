class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_s = {}
        word_t = {}
        for _ in s:
            if _ not in word_s:
                word_s[_] = 1
            else:
                word_s[_] += 1
        for _ in t:
            if _ not in word_t:
                word_t[_] = 1
            else:
                word_t[_] += 1
        if word_s == word_t:
            return True
        return False