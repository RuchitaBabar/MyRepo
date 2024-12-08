#nested if statement

age = 19
own_car = 'true'

# outer if statement
if (age>=18) :
     # inner if statement
     if (own_car == 'true') :
        print("you can drive your car")
         # inner else statement
     else  :
        print("Work hard and Purchase a new car")
        # outer else statement
else:
     print("You are under age")