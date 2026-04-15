# a="Hello world"
# print(a[:7])
# print(a[2:7]) #llo w
# print(a[::-1])

# List 

# l1=[
#     1,
#     1.1,
#     2,
#     2.2,
#     "one",
#     "two",
#     True,
#     False,
#     [7,8,9,[True,False,["five","six"]]]
#     ]
# print(len(["absdfhi"]))

# print(l1[3:4]) #2.2
# print(l1[-1][3][-1])
# print(len(l1))
# print(l1[-1][-1][-1][-1][-1])


# lis1.append("hi")
# lis1.append("hello")
# lis1.insert(1,0)
# lis1.extend([10,11,12])

# lis1.append("Hello")
# lis1.extend("Hello")

# lis1.remove(2)
# lis1.remove(2)
# lis1.pop(3)
# lis1.pop()
# lis1.pop()
# lis1.pop()
# lis1.pop()
# lis1.clear()
# lis1=[1,2,3,4,5,6,234,345,2,3,54]

# lis1[3]=44

# print(lis1)

# print(lis1[::-1])
# print(lis1.index(2345))
# print(lis1.count(2))

# lis1.sort()
# lis1.sort(reverse=True)
# lis1.reverse()
# print(lis1)

# Tuple 

t1=(1,2,1,3,2,3,21,3,45,4,2)

# t1[3]=333

# print(t1.count(2))
# print(t1.count(3))

# person=("Jimmy",45)
# name,age=person
# print(age)

# peapleData=[
#     ("Jimmy",45),
#     ("John",34),
#     ("Jane",23),
#     ("Jack",56),
#     ("Jill",67)
#     ]

# for i,j in peapleData:
#     print(i)
#     print(j)

# Set 

# s1={12,3,2,43,2,4}
# s2={3,4,5,6,7,8,9,10}

# s1.add(44)
# s1.update([1,2,3])

# s1.discard(444)
# s1.clear()
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s2.difference(s1))


# print(s1[3])

# for i in s1:
#     print(i)


# Dict 

d1={
    "name":"Jimmy",
    "age":45,
    "city":"New York",
    "hobbies":["reading","traveling","cooking"],
    "isMarried":True
}

# print(len(d1))
# print(d1["hobbies"][-1])
# d1["age"]=46
# d1["isGoodGuy"]=False
# print(list(d1.keys()))
# print(list(d1.values()))

# print(list(d1.items()))

# print(list(range(5,40)))

for i in d1:
    print(d1[i])