#!/usr/bin/python
## Example 1
## Dictionary

a={}
print(a)
print(type(a))
print(len(a))
b=dict()
print(b)
print(type(b))
print(len(b))
x={"python":99,"java":80,".net":75}
print(x)
print(len(x))
y={100:"spring",12.12:"django",True:"flask"}
print(y)
z={"java":1000,"hadoop":12.12,"python":True}
print(z)


## Example 2
## Duplicate values & duplicate keys
x={"django":99,"flask":85,"pyramid":85}
print(x)
y={"python":99,"java":80,"java":90}
print(y)
z={"hyd":[10,20,30],"bang":{40,50,60},(1,2,3):[70,80,90]}
print(z)



## Example 3
## adding the key values & modifing the key values & removing, coping the key values

x={"django":99,"flask":85,"pyramid":85}
print(x)
print(x["django"])
print(x.get("flask"))
x["flask"]=90
print(x)
x["gap"]=75
print(x)
x.pop("pyramid")
print(x)
x.popitem()
print(x)
y=x.copy()
print(y)
x.clear()
print(x)

## Example 4
## Apply the for loop on the directory
x={"django":99,"flask":85,"pyramid":85}
print(x)
for p in x:
    print(p)
k=x.keys()
for q in k:
    print(q)
v=x.values()
for r in v:
    print(r)
kv=x.items()
for a in kv:
    print(a[0],a[1])


## Example 5
## required keys are allowed or not allowed
x={"django":99,"flask":85,"pyramid":85}
print(x)
print("flask" in x)
for k,v in x.items():
    print(k,v)


## Example 6
## it is very important
x={"python":{"django":99,"flask":85},"java":{"spring":90,"struts":80}}
print(x)
for k,v in x.items():
    print(k)
    for p,q in v.items():
        print(p,q)
