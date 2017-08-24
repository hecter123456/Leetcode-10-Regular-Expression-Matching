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

class Solution():
    def isMatch(self, s, p):
        s = s[::-1]
        p = p[::-1]
        for i,j in itertools.zip_longest(range(len(s)), range(len(p))):
            if i is None or j is None or (s[i] != p[j] and p[j] != "."):
                return False
        return True

if __name__ == '__main__':
    unittest.main()
