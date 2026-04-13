# a=0

# while a>5:
#     print("Hi")
#     print("Hello")
#     print("-----------")
#     a-=1

# No of Execution = 0
# a = 0,1,2,3,4,5

# str1="Hello"

# for a in range(100,0,-1):
#     print(a)

# a=range(200)
# print(list(a))

# for i in range(200,301):
#     print(i)
#     if i<=250:
#         continue
    
# i=0

# while i<=100:
#     if i==50:
#         continue
#     print(i)
#     i+=1

# No of execution: inf
# i = 0,1.....49, 50, 50, 50..........

# for i in range(5):
#     for j in range(5):
#         print("Fool!")
#     print("Ball"+str(j))


# for i in range(6):
#     continue

# print(i)

for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print("* ", end="")
        elif i+j==6:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

# print("Hello", end="")
# print(123, end="")
# print(134)


# (1,1) (1,2) (1,3) (1,4) (1,5)
# (2,1) (2,2) (2,3) (2,4) (2,5)
# (3,1) (3,2) (3,3) (3,4) (3,5)
# (4,1) (4,2) (4,3) (4,4) (4,5)
# (5,1) (5,2) (5,3) (5,4) (5,5)