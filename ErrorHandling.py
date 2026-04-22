# print(9)

print(1)
print(2)
print(3)
print("Hello")
# Print(6)
# print(90+"")
# print(int("uygrft"))

# try:
#     print(7+"")
# except ZeroDivisionError:
#     print("You cannot perform this operation...!")
# except TypeError:
#     print("Cannot concar num with str")


try:
    inp1=int(input("Enter Num1: "))
    inp2=int(input("Enter Num2: "))
    print(inp1/inp2)
except ValueError:
    print("Invalid Numbers...!")
except ZeroDivisionError:
    print(f"{inp1} cannot be divided by {inp2}")
finally:
    print("It is over")




print(17)