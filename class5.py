#!/usr/bin/python

## Set object
#set objects can be created by using curly braces {} or by calling set functions

## Example 1
x={10,20}
print(x)
print(type(x))
print(len(x))
y=set()
print(y)
print(type(y))
print(len(y))
z={10,20,30,40,50}
print(z)
p={10,20,10,30,20}
print(p)
q={100,12.12,True}
print(q)




## Example 2
x=[10,20,30,10,20,10]
print(x)
y=set(x)
print(y)



## Example 3
## Mathametical set operations
x={10,20,30,40,50}
print(x)
x.add(60)
print(x)
y=x.copy()
print(y)
x.discard(30)
print(x)
x.remove(50)
print(x)
x.pop()
print(x)
x.clear()
print(x)



## Example 4
A={1,2,3,4,5}
print(A)
B={4,5,6,7,8}
print(B)
print(A|B)
print(A.union(B))
print(B|A)
print(B.union(A))
print(A&B)
print(A.intersection(B))
print(B&A)
print(B.intersection(A))
print(A-B)
print(A.difference(B))
print(B-A)
print(B.difference(A))
print(A^B)
print(A.symmetric_difference(B))
print(B^A)
print(B.symmetric_difference(A))




## Example 5
## Applying the loop, while loop, packing and unpacking
x={10,20,30,40,50}
print(x)
print(20 in  x)
print(400 in x)
for p in x:
    print(p)
y={100,12.12,True}
print(y)
a,b,c=y
print(a)
print(b)
print(c)




## Example 6
## set comprehensions
x={p for p in range(10)}
print(x)
y={q*q for q in range(10,20) if q%3==0}
print(y)
z={r for r in range(20,30) if r%2!=0}
print(z)

