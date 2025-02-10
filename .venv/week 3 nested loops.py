#for n in range(1,11,1):
#   for c in range(1,11,1):
#       result = c*n
#       print(f"{n} X {c} = {result} | ",end="")
#   print()

number_list=[1,5,7,9,3,5,8,6]
user_number = int(input("enter a number : "))
if user_number in number_list:
    print("the number is in the list ")
else:
    print("the number is not in the list")