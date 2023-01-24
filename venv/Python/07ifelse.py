#
celsius = 18
if celsius > 30:
    print('Hot ')
elif 30 >= celsius > 20:
    print('Good')
elif -273 < celsius <= 20:
    print('Cold')
else:
    print('Something went wrong!')

# nested if statements
drivers_licence = True
age = 17

if age > 17:
    if drivers_licence:
        print('You can drive car')
    else:
        print('You need to go to course')
else:
    print('you need to get older')

"""
conditional expressions are statements that define 
how our program will behave in certain situations.
 We use the keyword ‘if’ followed by a condition to 
 make sure the code only runs when the condition is True. 
 We can add an alternative condition with the keyword ‘elif’, 
 when the previous one was not true. And if none of the earlier 
 conditions were true, we can use the keyword ‘else’. 
 Finally, we can also place ‘if’ statements within other if statements."""