try:
    age=int(input("enter the age:"))
    if(age>7):
        print("you are eligible to play")
    else:
        print("you are not eligible to play")
except:
    print("invalid input")
finally:
    print("thank you for using our product")