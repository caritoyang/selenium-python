try:
    user_input1 = input("Please enter 1st number: ")
    user_input2 = input("Please enter 2nd number: ")
    c = int(user_input1) + int(user_input2)
    print(c)
except:
    print("Your input is incorrect, please enter correct data.")
finally:
    print("This code I want to execute always at the end.")