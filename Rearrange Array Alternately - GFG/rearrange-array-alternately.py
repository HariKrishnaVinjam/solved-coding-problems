#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        i = 0
        j = n-1
        ind = 0
        temp = []
        while i<=j:
            if ind%2 == 0:
                temp.append(arr[j])
                j = j-1
            else:
                temp.append(arr[i])
                i = i +1
            ind += 1
        # print(temp)
        for i in range(n):
            arr[i] = temp[i]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends