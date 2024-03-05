#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        if n == 1:
            return True
            
        ptr1, ptr2 = 0, 1
        
        while ptr2 < n:
            if arr[ptr1] > arr[ptr2]:
                return False
            
            ptr1 += 1
            ptr2 += 1
            
        return True
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Ends
