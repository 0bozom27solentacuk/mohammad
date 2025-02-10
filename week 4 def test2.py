def check_num(prompt):
    valid_input = False
    while not valid_input:
        user_input = input(f"enter your {prompt} : ")
        if user_input.isnumeric():
            valid_input = True
        else:
            print("you must enter a number w")
    return int(user_input)


bmi = check_num("weight in kg")/(check_num("height in cm")/100)**2
print(f"your BMI is {bmi}")