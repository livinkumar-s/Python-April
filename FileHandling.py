# file = open("text.txt")
# print(file)
# content = file.read()
# content = file.readline()
# content = file.readline()
# content = file.readline()

# content=file.readlines()[1]
# print(content)

# print(file.writable())

# file.write("fuyhqafuygtfqeufuyqefg")

# file.close()


# file = open("text.txt",'w')

# # print(file.writable())

# content='''
# MSD is a great batsman
# he is the best batsman in the world
# and he is the best captain in the world
# '''

# file.write(content)

# file.close()

# file = open("text2.txt",'a')

# # print(file.writable())

# content='''
# MSD is a great batsman
# he is the best batsman in the world
# and he is the best captain in the world
# '''

# file.write(content)

# file.close()

# import os 
# os.remove("text2.txt")

try:
    with open("text.txt") as file:
        content=file.write()
except FileNotFoundError:
    print()
except PermissionError:
    print()

