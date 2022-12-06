class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
		#Code here
        rows = len(grid)
        cols = len(grid[0])
        maxi = rows + cols
        dist = [[0]*cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                else:
                    if i > 0 and j>0:
                        dist[i][j] = dist[i-1][j]+1
                        dist[i][j] = min(dist[i][j], dist[i][j-1]+1)
                    elif j >0:
                        dist[i][j] = dist[i][j-1]+1
                    elif i >0:
                        dist[i][j] = dist[i-1][j]+1
                    else:
                        dist[i][j] = maxi

        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if i < rows-1:
                    dist[i][j] = min(dist[i][j], dist[i+1][j]+1)
                if j < cols-1:
                    dist[i][j] = min(dist[i][j], dist[i][j+1]+1)
        return dist

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends