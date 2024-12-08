#nested if statement

age = 17
own_car = 'false'

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
     print("Under age")