# While

import time
celsius = 10
while celsius < 50:


  if celsius > 30:
    print('Hot ')
  elif 30 >= celsius > 20:
    print('Good')
  elif -273 < celsius <= 20:
    print('Cold')
else:
    print('Something went wrong!')

print('Current tempature is', celsius)
celsius += 5
time.sleep(1)

# The sleep function tells Python to
# wait 1 second so that the program
# can continue
