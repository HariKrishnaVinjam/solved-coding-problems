#User function Template for python3
from collections import deque
class Solution:

    def buildLowestNumber(self, S,N):
        # code here
        stack = deque()
        for i in S:
            while N>0 and stack and stack[-1]>i:
                stack.pop()
                N -= 1
            stack.append(i)
        if N>0:
            while N != 0:
                stack.pop()
                N -= 1
        res = ""
        while stack:
            res += stack.popleft()
        return str(int(res)) if res else "0"
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        S = input()

        solObj = Solution()

        print(solObj.buildLowestNumber(S,N))
# } Driver Code Ends