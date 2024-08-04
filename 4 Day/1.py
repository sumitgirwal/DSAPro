# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        low, high = 0, n-1
        while low<=high:
            mid = (low+high)//2
            if (mid == 0 or arr[mid-1]<=arr[mid]) and (mid == n-1 or arr[mid+1]<=arr[mid]):
                return mid
            elif mid>0 and arr[mid]<arr[mid-1]:
                high = mid-1
            else:
                low = mid+1
        return 0


 
 
 
