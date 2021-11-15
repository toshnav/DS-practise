a = []
n = int(input(" Enter the Number oif sorting elements \n "))
for i in range(n):
    t = int(input("element No. " + str(i) + "\n"))
    a.append(t)
for j in range(1,len(a)):
    key = a[j]
    i = j - 1
    while(i >= 0 and a[i] > key ) :
        a[i + 1] = a[i]
        i = i - 1
    a[i + 1] = key
print(a)

"""" 
In the Insertion Sort is like arranging the playing cards in a sorted order:
1) Time complexity of insertion sort is : No. of Comparisons + No. of Movemnets Shift 
2) The Worst case Time complexity of Insertion Sort : O(n^2)  
3) The Best case Time complexity of Insertion Sort : Omega Ω(n)

"""