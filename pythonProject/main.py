def sort(a):
    for i in range(1,5):
        j=i-1
        k=a[i]
        while(j>=0 and a[j]<k):
            a[j+1]=a[j]
            j-=1
        a[j+1]=k

a=[0,1,3,6,10]
sort(a)
print(a)