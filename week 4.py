valid_input = False
while not valid_input :
    height = input("enter your height : ")
    if height.isnumeric():
        valid_input = True
    else :
        print("you must enter a number !!!")
print(height)
valid_input = False
while not valid_input :
    weight = input("enter your weight : ")
    if height.isnumeric():
        valid_input = True
    else :
        print("you must enter a number !!!")
print(weight)
bmi = int(weight)/int(height)/100**2
print(f"your bmi is {bmi}")