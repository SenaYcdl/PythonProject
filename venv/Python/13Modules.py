
def greeting(name):
    print('Hello', name)

    import test
    test.greeting('Sena')



#We need to import the seaborn library

#import seaborn as sns

#Weather data
day = [1, 2, 3, 4, 5, 6, 7]
avg_temperature = [14,9,3,11,18,27,6]

#Create a bar plot for the given data


"""
Seaborn kütüphanesi. Bu kütüphane istatistiksel grafikler 
oluşturmamızı sağlar ve veri görselleştirmede oldukça popülerdir.
Öncelikle kütüphanemizi kurmamız gerekiyor. Bunu yapmak için 
“!pip install” yazıyoruz ve ardından kütüphanenin adını yazıyoruz. 
Eğer böyle bir mesaj görürseniz kütüphane kurulmuş demektir. 

import ifadesinden sonra neden 
"as sns" ifadesini eklediğimizi merak edebilirsiniz. 
Bu, kitaplık adları için takma adlar oluşturmak için 
kullandığımız Python'un harika özelliklerinden biridir. 
Bu kütüphanelerin metotlarına erişmek istediğimizde tam 
adını yazmak zorunda değiliz, bunun yerine kısa takma adlarını kullanabiliriz.

Bu örnekte, seaborn'u çağırmak için sadece 
"sns" yazıyoruz. Daha fazla konuşmadan kodlamaya 
başlayalım! Belirli verilerin grafik görselleştirmesini 
oluşturan bir program yazacağız. Bu durumda 7 veri noktasından 
oluşan bir çizgi grafiği oluşturmak istiyoruz, bu yüzden içinde 
bu sayıların olduğu bir liste oluşturuyoruz. 
Gördüğünüz sayılar bizim y koordinatlarımızdır.

Ardından, seaborn kütüphanesinin bir yöntemini kullanacağız. 
Buna “lineplot” denir ve adından da anlaşılacağı gibi 
bir çizgi grafiği oluşturur. “sns.lineplot” yazıyoruz ve 
parantez içinde verilerimizi vermemiz gerekiyor. 
“data” listesinin içinde y koordinatlarımız var, 
bu yüzden bu listenin adını yazıyoruz. Ama bildiğiniz 
gibi, bir grafik oluşturmak için karşılık gelen x 
değerlerine de ihtiyacımız var.
Bunlar için ayrı bir liste oluşturmak yerine, 
range() işlevini kullanarak 0'dan 6'ya
kadar bir sayı dizisi oluşturabiliriz. 
lineplot() yönteminde önce x-koordinatlarımızı, 
ardından y-koordinatlarımızı ekliyoruz."""