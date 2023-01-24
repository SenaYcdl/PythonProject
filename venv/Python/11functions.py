# You can think of them like
# functions in math. In an expression
# like this: f(x) = x^2 + 3x, whatever
# number we substitute for x, the
# relevant operation is performed,
# and the result is given to us.
# It’s pretty similar in Python.

def hello(name):
    print('hello', name)


hello('Sena')

"""
Bir fonksiyon tanımlarken önce “def” anahtar kelimesini 
ardından fonksiyonun amacına uygun bir isim yazıyoruz. 
Ayrıca parantez içinde bir argüman belirtiriz.
Bu örnekte "merhaba", işlevin adıdır ve "name" argümandır. 
Argümanları az önce gördüğümüz matematiksel 
fonksiyondaki x olarak düşünebilirsiniz. 
Fonksiyonlara değer vermek için kullanılırlar. 
Argümanı ekledikten sonra iki nokta üst üste 
koyup fonksiyona ait kodu girintiliyoruz. 
Bu örnekte, fonksiyonumuzun "Merhaba" ve ardından 
bir ad yazdırmasını istiyoruz"""


def sum(num1, num2):
    print(num1 + num2)
sum(3, 5)

# functions are small pieces of code that are designed
# to perform specific tasks. They can be built-in
# or user-defined, and they help our programs to
# be non-repetitive and well organized.
#işlevler, belirli görevleri gerçekleştirmek
# için tasarlanmış küçük kod parçalarıdır.
# Yerleşik veya kullanıcı tanımlı olabilirler
# ve programlarımızın tekrarlanmayan ve
# iyi organize edilmiş olmasına yardımcı olurlar.


def sum2(number1,number2):
    answer=number1+number2
    return answer
result=sum2(3,5)
print(result)