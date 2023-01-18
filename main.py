print("Welcome!")
print("For each correct ans you will get Rs. 100")
print("Rules:\n1. There are 3 Questions each question has 4 options\n2. Options need to be selected by their respective No.\n")


# def match(x):
#     x = int(input("Enter your choice"))
#     match x:
#         case 1:
#             print("You've chooses Option 1")
#         case 2:
#             print("You've chooses Option 2")
#         case 3:
#             print("You've chooses Option 3")
#         case 4:
#             print("You've chooses Option 4")

TOTAL = 0

def increment():
    global TOTAL
    TOTAL = TOTAL + 100

que1 = ["Question 1: Who is the Prime Minister of India?"]
ans1 = ["Options :", "1. ABC", "2. N. Modi", "3. XYZ", "4. MMT"]
print(que1)
print(ans1)

x = int(input("Enter your choice:"))
if (x == 1):
    print("Incorrect\n")
elif (x == 2):
    print("It is Correct, You've won Rs. 100\n")
    increment()
elif (x == 3):
    print("Incorrect\n")
elif (x == 4):
    print("Incorrect\n")
else:
    print("Invalid\n")

que2 = ["Where is Delhi Located?"]
ans2 = ["1. India", "2. ABC", "3. XYZ", "4. ZXC"]
print(que2)
print(ans2)

x = int(input("Enter your choice:"))
if (x == 1):
    print("Correct, You've won Rs. 100\n")
    increment()
elif (x == 2):
    print("It is incorrect\n")
elif (x == 3):
    print("Incorrect\n")
elif (x == 4):
    print("Incorrect\n")
else:
    print("Invalid\n")

que3 = ["Example of greeting"]
ans3 = ["1. xyz", "2. NMC", "3. Hello", "4. UIO"]
print(que3)
print(ans3)

x = int(input("Enter your choice:"))
if (x == 1):
    print("Incorrect\n")
elif (x == 2):
    print("It is Incorrect\n")
elif (x == 3):
    print("Correct, You've won Rs. 100\n")
    increment()
elif (x == 4):
    print("Incorrect\n")
else:
    print("Invalid\n")

print("You've Won Rs.", TOTAL)

