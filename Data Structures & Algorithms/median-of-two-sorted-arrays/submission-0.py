class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=[]
        i=0
        j=0
        n=len(nums1)
        m=len(nums2)
        while i<n and j<m:
            if nums1[i]<nums2[j]:
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        while i<n:
            arr.append(nums1[i])
            i+=1
        while j<m:
            arr.append(nums2[j])
            j+=1
        total=m+n
        mid=total//2
        if total%2==1:
            return float(arr[mid])
        else:
            return float((arr[mid]+arr[mid-1])/2)