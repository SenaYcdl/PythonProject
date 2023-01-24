def divide(number1, number2):
    number1_integer = int(number1)
    number2_integer = int(number2)

    return number1_integer / number2_integer


number1 = input('Please provide number1: ')
number2 = input('Please provide number2: ')
print(divide(number1, number2))


# bu kodda integer degerler istiyor ama kullanici string degerde girebilir bu yuzden valueError hatasi verir
# bunun onune gecmek icin try/except kullanilir

# def divide(number1,number2):
#    try:
#    number1_integer = int(number1)
#    number2_integer = int(number2)
#    return number1_integer / number2_integer
#
#  except:
#  return 'Only integers are allowed! Try again'
#
# number1= input('Please provide number1: ')
# number2= input('Please provide number2: ')


def divide(number1, number2):
    try:
        number1_integer = int(number1)
        number2_integer = int(number2)
        return number1_integer / number2_integer

    except ValueError:
        return 'Only integers are allowed! Try again'

    except ZeroDivisionError:
        return 'You cannot divide any number by zero!'

    number1 = input('Please provide number1: ')
    number2 = input('Please provide number2: ')

    print(divide(number1, number2))


"""
Bir sayıyı 0'a bölmeye çalışırsak, normalde bir ZeroDivisionError alırız. 
Hatırlayacağınız gibi, bir dize girerken sahip olduğumuz istisna bir ValueError idi. 
Programımızda farklı istisna blokları belirtmek için farklı hata türlerini kullanabiliriz. 
Bunu yapmak için her bir hariç anahtar kelimeden sonra hata türünü eklememiz gerekir.

Bu yüzden burada daha önce yaptığımız gibi bir ValueError için bir istisna bloğu ve bir ZeroDivisionError 
için bir tane daha ekliyoruz. Şimdi programı çalıştırdığımızda iki farklı hata için farklı mesajlar veriyor.

"""