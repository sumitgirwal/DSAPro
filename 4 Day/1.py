class Solution:
    def peakElement(self, arr, n):
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            
            # Check if mid is a peak element
            if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
                return mid
            # If the element on the left is greater, move to the left half
            elif mid > 0 and arr[mid - 1] > arr[mid]:
                high = mid - 1
            # Otherwise, move to the right half
            else:
                low = mid + 1

# Example usage:
# sol = Solution()
# arr = [1, 3, 20, 4, 1, 0]
# n = len(arr)
# print(sol.peakElement(arr, n))  # Output: Index of a peak element, e.g., 2
