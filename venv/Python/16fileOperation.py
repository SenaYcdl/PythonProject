
#message_file = open("venv/Python/16file.txt")

message_file = open("16file.txt", "r")

content = message_file.read()
message_file.close()

print(content)

#txt file olusturmak icin("w" ile otomatik file olusturabiliyoruz)
hello_file= open("hello.txt", "w")

#txt file a otomatik olarak metin gondermek icin
hello_file.write('Hello World, this is Python')
hello_file.close()


import random

#numbers_file = open('number_history.txt', 'w')
with open('number_history.txt', 'w') as numbers_file:

 while True:

    random_number=random.randrange(1000)
    print(random_number)
    numbers_file.write(str(random_number))
    numbers_file.write('\n')

    if random_number == 777:
        print('Found!')
        break


"""
Öncelikle size bir örnek üzerinden göstereyim. “with” kullandığımızda, 
dosyamızı kapatmak için bir ifade eklememize gerek yoktur. Ancak bu komutu atlarsak, 
Python dosyanın kapatılması gerektiğini nereden biliyor? Aslında oldukça kolay. Dosyayı açarken dosyayı bir 
değişkene atamak yerine “with” yazıp ardından open() fonksiyonuna geçiyoruz. Ardından, "as" ve dosya için 
referansımız olacak bir tanımlayıcı yazıyoruz.

İşte önemli kısım geliyor. with ifadesinden sonra, bir kapsam oluşturmak için kodu girintiliyoruz. 
Python yorumlayıcısı bu kapsam içindeyken dosya açık kalır. with-scope'un sonuna gelip çıktıktan sonra, 
Python dosyayı bizim için otomatik olarak kapatacaktır.

Özetlemek gerekirse, dosyalar harici bilgileri ve verileri depolamak veya bunlara erişmek için kullanılır. 
Bir dosyayı yazma ve okuma gibi farklı modlarda açmak için open() işlevini kullanabiliriz. 
Ve son olarak, dosyalarımızı kullandıktan sonra kapattıklarından emin olmak için with anahtar kelimesini kullanabiliriz.


"""


