def maximum(maxi,x,n,i):
    if i==n:
        return maxi
    if maxi<x[i]:
        return maximum(x[i],x,n,i+1)
    else:
        return maximum(maxi,x,n,i+1)
def minimum(mini,x,n,i):
    if i==n:
        return mini
    if mini>x[i]:
        return minimum(x[i],x,n,i+1)
    else:
        return minimum(mini,x,n,i+1)
def main():
    n=int(input("enter any number"))
    x=[]
    for i in range(n):
        x.append(int(input("enter any value")))
    print("the maximum value is",maximum(x[0],x,n,1))
    print("the minimum value is ",minimum(x[0],x,n,1))
main()