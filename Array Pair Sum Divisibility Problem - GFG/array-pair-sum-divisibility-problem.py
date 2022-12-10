#User function Template for python3

class Solution:
	def canPair(self, nuns, k):
		# Code here
		d = {}
		for i in nuns:
		    if i%k in d:
		        d[i%k] += 1
		    else:
		        d[i%k] = 1
	    
	    if 0 in d:
	        if d[0]%2 != 0:
	            return False
	    
	    for i in range(1,k):
	        if i in d:
	            if k-i in d:
	                if d[i] != d[k-i]:
	                    return False
	            else:
	                return False
	    return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends