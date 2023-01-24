def argument_printer(arg_position1, arg_position2):
    print('Argument at position 1:', arg_position1)
    print('Argument at position 2:', arg_position2)

argument_printer('value 1', 'value 2')

"""
Bu fonksiyonun içinde iki adet print fonksiyonumuz var.
Biri birinci konumdaki bağımsız değişkeni yazdırmak için, 
diğeri ikinci konumdaki bağımsız değişkeni yazdırmak için. 
Şimdi fonksiyonu çağıralım ve birinci argüman için “value 1”,
ikinci argüman için “value 2” verelim. Çıktımız aşağıdaki 
gibi olacaktır. Python, işlevi tanımlarken argümanları koyduğunuz 
sırayla değerleri atar. Burada Python'un ilk değeri birinci argümana 
ve ikinci değeri ikinci argümana atadığını görebilirsiniz. 
Argümanları konumlarına göre senkronize etmeye -positional argument- denir."""


# Argument at position 1: value 1
# Argument at position 2: value 2


def greeting(first_name, last_name, auto_correction):
    if auto_correction == True:
        capitalised_first_name = first_name.capitalize()
        capitalised_last_name = last_name.capitalize()
        print("Hello,", capitalised_first_name, capitalised_last_name)
    else:
        print("Hello,", first_name, last_name)


greeting('Sena', 'YuceDaL', True)

"""
“greeting” adında bir fonksiyon ve 
first_name, last_name ve “auto_correction” 
adında 3 adet argüman tanımlıyoruz. Bu koşul True ise, 
“capitalize()” yöntemi ad ve soyadların 
ilk harflerini büyük yapar. False değerine sahipse,
ad ve soyadlar girildikleri gibi yazdırılacaktır.
değişkenimiz True olduğundan, 
Python hem adların hem de soyadların 
ilk harflerini büyük yazacaktır. 
False değerini atarsak, isimler girildiği gibi yazdırılacaktır."""


def car(brand, model, colour):
    print('My favorite car is the', brand, model, 'in the colour', colour)


car('Audi', 'R8', 'black')
car(colour='pink', model='R8', brand='volvo')

# Scope
"""
number = 13  # global variable
def change_number():
    number = 4  # local variable
change_number()
print(number)"""

number = 13  # global variable


def change_number():
    global number
    number = 4  # local variable


change_number()
print(number)


# bir fonksiyon tanımlayarak yerel
# bir kapsam yarattığımızı söyleyebiliriz.
# Global kapsamda tanımlanan değişkenlere
# kodun tamamından erişilebilirken,
# yerel kapsamdaki değişkenlere yalnızca kendi bölgelerinden erişilebilir.

def greetings(a, b, c=5, d=2):
    if c > d:
        print(a)
    else:
        print(b)


greetings(a=0, b=1, d=4)
price = 1200


def update_price(new):
    price = new
    return price


update_price(1500)
print(price)

num1 = 8
num2 = 4

""""
def function():
    num1 = 12
    return num1 + num2
print(function())"""