#User function Template for python3
class Solution:
	def addBinary(self, A, B):
	    
		# code here
		
		ind = 0

		for i in range(len(A)):
		    if A[i] == '0':
		        ind += 1
		    else:
		        break
		A = A[ind:]

		ind = 0
		

		for i in range(len(B)):
		    if B[i] == '0':
		        ind += 1
		    else:
		        break
		B = B[ind:]
		
# 		print(A, B)
		
		carry = '0'
		len_A = len(A)
		len_B = len(B)
		
		if len_A > len_B:
		    B = '0'*(len_A - len_B) + B
		  #  print("B=", B)
		elif len_B > len_A:
		    A = '0'*(len_B - len_A) + A 
		  #  print("A=", A)
		
		
		res = ""
		for i in range(len(A)-1, -1, -1):
		    if A[i] == '0' and B[i] == '0':
		        if carry == '0':
		            res += '0'
		        else:
		            res += '1'
		            carry = '0'
		    elif (A[i] == '1' and B[i] == '0') or (A[i] == '0' and B[i] == '1'):
		        if carry == '0':
		            res += '1'
		        else:
		            res += '0'
		            carry = '1'
		    else:
		        if carry == '0':
		            res += '0'
		            carry = '1'
		        else:
		            res += '1'
		            carry = '1'
		        
        if carry == '1':
            res += '1'
        
        return res[::-1]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		a,b = input().split(" ")
		ob = Solution()
		answer = ob.addBinary(a,b)
		
		print(answer)


# } Driver Code Ends