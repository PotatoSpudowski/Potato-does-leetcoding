"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]


 

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
"""


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A)<3:return False
        l=len(A)
        i,j=0,l-1
        while i<j and A[i]<A[i+1]:
            i+=1
        while j>0 and A[j]<A[j-1]:
            j-=1
        if i==j and j!=l-1 and i!=0:
            return True
        
        return False