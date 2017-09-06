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
        if "*" and "." in s:
            return False
        table = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        table[0][0] = True
        for j in range(2,len(p) + 1):
            table[0][j] = p[j-1] == "*" and table[0][j-2]
        for i in range(1,len(s)+1):
            for j in range(1, len(p)+1):
                if(p[j-1] == "*"):
                    table[i][j] = table[i][j-2] or (s[i-1] == p[j-2] or p[j-2] == ".") and table[i-1][j]
                else:
                    table[i][j] = table[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == ".")
        return table[-1][-1]

if __name__ == '__main__':
    unittest.main()
