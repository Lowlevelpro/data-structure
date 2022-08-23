def heapify(arr,m,i):
     large=i
     l=2*i+1
     r=2*i+2

     if l<m and arr[large]<arr[l]:
         large=l

     if r<m and arr[large]<arr[r]:
         large=r

     if large!=i:
         arr[i],arr[large]=arr[large],arr[i]
         heapify(arr,n,large)


arr=[3,20,4,50,4,21,34,21,43,2,55]
n=len(arr)
m=(n//2)-1

for i in range(m,-1,-1):
     heapify(arr,n,i)

def heapsort(arr,size):
    for i in range(size-1,-1,-1):
       arr[0],arr[i]=arr[i],arr[0]
       heapify(arr,i,0)

heapsort(arr,n)

print(arr)
