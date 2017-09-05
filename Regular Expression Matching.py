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
    def testStarDot(self):
        s = "ab"
        p = ".*"
        Ans = True
        self.assertEqual(Solution().isMatch(s,p),Ans);

class Solution():
    def isMatch(self, s, p):
        if (not p):
            return not s
        if (len(p) > 1 and p[1] == "*"):
            return self.isMatch(s,p[2:]) or s and self.isMatch(s[1:],p) and (s[0] != "." and s[0] != "*" and (s[0] == p[0] or '.' == p[0]))
        else:
            return s and (s[0] != "." and s[0] != "*" and (s[0] == p[0] or '.' == p[0])) and self.isMatch(s[1:],p[1:])

if __name__ == '__main__':
    unittest.main()
