class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        array=[1]*(n+m-1)
        for i in range(1,n+m-1):
            array[i]=i*array[i-1]
        return (array[-1]//(array[n-1]*array[m-1]))
        