""" 
1 ) Quik Sort is a Divide and Conqure Apporach just like Merge Sort.
2 ) Quik Sort uses the Partitioning techinique while sorting.
3 ) Time Taken to travel and partition the given array linear which is O(n).
4 ) The key (Pivot )can be choosen as any element.
5 ) Average Case Space Complexity : O(log(n)).
6 ) Worst Case Space Complexity : O(n).
7 ) Average Case Time Complexity : O(log(n)).
8 ) Worst Case Time Complexity : O(n^2).
8 ) Best Case Time Complexity : O(n logn  ).

Partitioning :

let A = [,,,,,,,,]
n = len(A)
key =  A[len(A)]
i = p-1
for j in range(0,n-2): 
    if A[j] <= key :
        i = i + 1 
        Exchange A[i] both with each other A[j]
Exchange 
A[i+1] = A[r]
return


QUICKSORT :
if p < r :
    q = Parttion(A,p,r)
    QuickSort(A,p,q-1)
    QuickSort(A,q+1,r)
"""
def Partition(A,p,r) :
    i = p-1
    key = A[r]
    for j in range(p,r):
        if A[j] <= key :
            i = i + 1
            A[i] ,A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return (i+1)

def QuickSort(A,p,r):
    if len(A) == 1:
        return A
    if p < r :
        q = Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)

A=[20,40,93,65,34,45]
n = len(A)
QuickSort(A,0,n-1)
print(A)


