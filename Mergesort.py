def Merge(A , p ,q , r ):
    n1 = q - p + 1
    n2 = r - q
    L=[0]*n1
    H=[0]*n2
    for i in range(0,n1) :
        L[i] = A[p+i]

    for j in range(0,n2) :
        H[j] = A[q+j+1]

    i = 0 
    j = 0
    k = p 
    while i < n1 and j < n2 :
        if L[i] <= H[j]:
            A[k] = L[i]
            i = i +1
        else:
            A[k] = H[j]
            j = j + 1
        k = k + 1
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        A[k] = H[j]
        j += 1
        k += 1

def MergeSort(A,p,r):
    if p < r :
        q = p + (r-1)//2
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A,p,q,r)
A=[120,30,40,56,99,34]
n = len(A)
MergeSort(A,0,n-1)
print(A)

