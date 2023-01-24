#Dictionaries

"""
Lists ve tuples gibi dictionaries de birden çok öğeyi farklı bir biçimde tutabilir.
Dictionary içindeki her öğe bir key/value çiftinden oluşur. Key i değerin indeksi olarak düşünebilirsiniz.
"""


phone_book={'Sena Yucedal' : '73789011', 'Selin Demir': '9827834647', 'Ali Can': '39847832'}
print(phone_book)

print(phone_book['Sena Yucedal'])



inventory = dict()
inventory['bananas'] = 25
inventory['apples'] = 102
inventory['oranges'] = 4
inventory['watermelons'] = 100

print(inventory)

#keys
print(inventory.keys())

#values
print(inventory.values())

#items
print(inventory.items())

#for ile tum elementleri yazdir
for element in inventory:
    print(element)

#ikinci yol
for key in inventory:
    inventory[key] += 100
    print(inventory)


#hepsi bir arada
for key,value in inventory.items():
    if value > 200:
        print('Too many', key)
    else:
        print('Enough', key)


#dictionaries could hold multiple elements like lists and tuples,
# but in a different format and each element inside a dictionary consists of a key/value pair.