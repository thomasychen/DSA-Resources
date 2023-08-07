# DSA-Resources
Key implementation notes for important algorithms:

Binary Search: 
l, r = 0, len(nums)-1
while l<=r:
    m = (l+r)//2
    if nums[m] < target:
        l = m + 1
    elif nums[m] > target:
        r = m-1
    else:
        return m

Useful for median of 2 sorted arrays, you can eliminate a section of one of the arrays given each condition

Arrays and 2 pointers:
product of array except self and trapping rain water both use (left) and (right) condition arrays and then combine them

Use freq arrays for fixed alphabet questions, and sliding windows for substring qs that aren't dp

BFS:
Visited gets initialized with initial node and at time of queue append, while in djikstras you do not do this, you only add to visited on time of queue pop

Backtracking: Keep a nonlocal result array and DFS

Kth largest element is faster with quicksort than heap (avg n vs nlogn)
