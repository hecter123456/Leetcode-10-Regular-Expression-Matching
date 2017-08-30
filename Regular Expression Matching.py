import unittest
import itertools

class unitest(unittest.TestCase):
    def testDiffLength(self):
        s = "aa"
        p = "a"
        Ans = False
        self.assertEqual(Solution().isMatch(s,p),Ans);
    def testSameString(self):
        s = "aa"
        p = "aa"
        Ans = True
        self.assertEqual(Solution().isMatch(s,p),Ans);
    def testSameLength(self):
        s = "ab"
        p = "aa"
        Ans = False
        self.assertEqual(Solution().isMatch(s,p),Ans);
    def testDot(self):
        s = "ac"
        p = "a."
        Ans = True
        self.assertEqual(Solution().isMatch(s,p),Ans);
    def testInvalidInput(self):
        s = "a."
        p = "a."
        k = "a*"
        g = "a*"
        Ans = False
        self.assertEqual(Solution().isMatch(s,p),Ans);
        self.assertEqual(Solution().isMatch(k,g),Ans);
    def testStar(self):
        s = "aa"
        p = "a*"
        Ans = True
        self.assertEqual(Solution().isMatch(s,p),Ans);
    def testStarDiffLength(self):
        s = "aab"
        p = "c*a*b"
        Ans = True
        self.assertEqual(Solution().isMatch(s,p),Ans);
    def testLongInput(self):
        s = "abcd"
        p = "d*"
        Ans = False
        self.assertEqual(Solution().isMatch(s,p),Ans);

class Solution():
    def isMatch(self, s, p):
        s = s[::-1]
        p = p[::-1]
        i, j = 0, 0
        while j < len(p):
            while j < len(p) and p[j] == "*":
                j += 1
                temp = p[j]
                if j == len(p):
                    return False
                if i < len(s) and (s[i] == "*" or s[i] != p[j]):
                    return False
                while i < len(s) and s[i] == temp:
                    i += 1
                while j < len(p) and p[j] == temp:
                    j += 1
            if j == len(p):
                break
            if i < len(s):
                if s[i] == "*" or s[i] == "." or (s[i] != p[j] and p[j] != "."):
                    return False
            if i < len(s):
                i += 1
            j += 1
        if i == len(s):
            return True
        return False

if __name__ == '__main__':
    unittest.main()
