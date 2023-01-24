#append
shooping_list=['Apple', 'Juice', 'Ball', 'Book']
shooping_list.append('Water')
print(shooping_list)


#insert
shooping_list.insert(2,'Banana')
print(shooping_list)


#remove
shooping_list.remove('Apple')
print(shooping_list)


#index
shooping_list[3]="Strawberry"
print(shooping_list)


#sayilar icin
number_list=[1,2,3,4,5]

square_list= []

for num in number_list:
    square_list.append(num**2)

    print(square_list)


#daha az kodla
number_list=[1,2,3,4,5]
square_list = [num**2 for num in number_list]
print(square_list)

#List==>mutable
#Tuples==>immutable

#list den cikarip yazdirma
shooping_list=['Apple', 'Juice', 'Ball', 'Book']

item1, item2, item3, item4 = shooping_list
print(item1)
print(item2)
print(item3)
print(item4)

print(shooping_list[0])
print(shooping_list[1:3])


#Bu ornekte hata aliriz
shooping_list[1]="Water"

#Tuple tipinin değişmez olduğundan bahsetmiştik. 
# Bir öğeyi değiştirmeye çalışarak bunu test ettik(1.indexi water ile degistrimeye calistik)
# Bu kodu çalıştırdığımızda bir hata alıyoruz. Hata mesajında da görebileceğiniz gibi,
# tuple'lara yeni elemanlar atayamayız. Bir tuple in elemanlarına erişebiliriz ama onları değiştiremeyiz.

