def binary_search(l,h,key,x):
   if l>h:
      return -1
   mid=(l+h)//2
   if key==x[mid]:
      return mid
   if key>x[mid]:
      return binary_search(mid+1,h,key,x)
   if key<x[mid]:
      return binary_search(l,mid+1,key,x)
def main():
   n=int(input("enter number of elements"))
   x=[]
   for i in range(n):
      x.append(int(input("enter the value")))
   key=int(input("enter value to search"))
   f=binary_search(0,n-1,key,x)
   if f==-1:
      print("value not found")
   else:
      print("value found at the position ",f+1)
main()