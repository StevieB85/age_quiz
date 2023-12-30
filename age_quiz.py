# need to establish the persons aged
name = input("Please enter your name : ")
# using the input function i can get this information 
age = int(input("please provide us with your age : "))

# if the person inputs any of the relevent ages they will receive the following responses 
print(f"Wow {name}")

if age < 13:
    print("you qualify for the kiddies discount")
elif age >= 100:
    print("Sorry, you're Dead")
elif age > 65:
    print("Enjoy your retirement!")
elif age > 40:
    print("you've over the hill.")
elif age == 21:
    print("Congrats on your 21st")
else:
    print("age is just a number.")
        
