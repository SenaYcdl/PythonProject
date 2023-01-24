#Data Types
"""
String
Numbers : There are basically three number data types. These are integers, floating-point numbers, and complex numbers.
Lists : Lists can hold multiple elements of the same or even different types of data together.

"""

store_items = ['Apple' , 1.49 , 'Banana' , 1 , 'Milk' , 2.99 , 'Cheese' , 4.49]
print(store_items, type(store_items))

print(store_items[2]) #2. indexi yazdirir

print(store_items[0:4]) #ilk indexi dahil 4. index dahil degil

print(store_items[2:]) #ilk iki index haric gerisini yazdir

print(store_items[:2]) #2.index ve sonrasini yazdirma


#Data Type Conversion

store_items[2] = 'Chocolate'
print(store_items)


#String i int e cevirme
age = '25'
print(type(age))

age= int(age)
print(age, type(age))