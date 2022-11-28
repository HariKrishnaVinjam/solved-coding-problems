#User function Template for python3

class Solution:

	def findSubarray(self,a, n):
	    start_index = 0
	    end_index = 0
	    
	    overall_sum = 0
        sum = 0
        i = 0
        while i < n:
            if a[i] > -1:
                j = i
                while j<n and a[j] > -1:
                    sum += a[j]
                    j += 1
                
                if sum > overall_sum:
                    overall_sum = sum
                    start_index = i
                    end_index = j
                elif sum == overall_sum:
                    if (j-i) > (end_index - start_index):
                        start_index = i
                        end_index = j
                i = j
            else:
                sum = 0
                i += 1
        
        if start_index == 0 and end_index == 0:
            return [-1]
        else:
            return a[start_index:end_index]
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    a=list(map(int, input().strip().split()))
	    ob = Solution()
	    ans=ob.findSubarray(a, n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends