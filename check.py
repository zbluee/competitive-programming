#User function Template for python3
from collections import Counter

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        count_a = Counter(A)
        count_b = Counter(B)
            
        for b in B:
            if count_a[b] != count_b[b]:
                return False
                
        return True
    
                
        #return: True or False
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends
