# math modülü matematiksel işlemler yapmanızı kolaylaştırmak için yazılmış bir modüldür.
import math

# math.ceil()
# Verilen ondalıklı sayıyı bir üst sayıya çevirir.
# Sayı eğer tam sayı ise __ceil__ fonksiyonundan yararlanır.
print(math.ceil(32.05))
print("-------------------------------")

# math.floor() ceil fonksiyonunun tam tersi bir işleve sahip.
# Verilen ondalıklı sayıyının bir altındaki tam sayıyı döndürür.
print(math.floor(89.82))
print("-------------------------------")

# math.copysign()
# Aldığı iki parametreden ikincisinin işaretini birincisine verir.
print(math.copysign(-12, 25))
print("-------------------------------")

# math.fabs()
# Verilen değerin mutlak değerini alır. abs den farklı.
# Çıktısını tam sayı olarak değil ondalıklı sayı olarak döndürüyor.
print(math.fabs(-388))
print(abs(-889))
print("-------------------------------")

# math.factorial()
# Verilen sayının faktoriyelini döndürüyor.
print(math.factorial(44))
print("-------------------------------")

# math.gamma()
# Bu fonksiyon factorial fonksiyonuna çok benziyor.
# Farklarından biri verilen sayının bir azının faktoriyelini hesaplamasıdır.
# Ancak asıl fark sayı büyüdüğünde ortaya çıkıyor.
print(math.factorial(35))
print(math.gamma(35))
print("-------------------------------")

# math.fmod()
# Verdiğiniz birinci parametrenin ikinci parametreye bölümünden kalanı buluyor.
print(math.fmod(78784, 11))
print("-------------------------------")

# math.fsum()
# sum fonksiyonundaki bir açığı kapatıyor.
# sum fonksiyonu ondalıklı sayılarla çalışırken biraz sorun çıkarabiliyor.
print(math.fsum([865, 64, 4, 44, 489, 49, 46, 44, 63]))
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print("-------------------------------")

# math.gcd()
# Verilen iki sayının EBOB’unu veriyor
print(math.gcd(85, 95))
print("-------------------------------")

# math.trunc()
# int fonksiyonu ile aynı işi yapıyor.
print(math.trunc(789.4545))
print(int(848.5))
print("-------------------------------")

# euler sabitini tutan bir değişken. Değeri: 2.718281…
# pi sayısını tutan değişken. Değeri: 3.141592….
print(math.e)
print(math.pi)
print("-------------------------------")

# math.exp()
# euler sabitinin kuvvetini alır. Yani yaptığı iş şudur:math.e ** x
print(math.exp(8))
print("-------------------------------")

# math.log()
# Birinci değerin ikinci değere göre logaritmasını hesaplar.
print(math.log(2, 10))
print("-------------------------------")

# math.log1p()
# Verilen sayının bir fazlasının e tabanına göre logaritmasını hesaplar.
# math.log2()
# Verilen sayının 2 tabanında logaritmasını hesaplar.
print(math.log1p(10))
print(math.log2(2))
print("-------------------------------")

# math.pow()
# ** ve gömülü fonksiyonlardan pow ile aynı işi yapıyor.
# Yani birinci sayının ikinci sayıya göre kuvvetini alıyor.
print(math.pow(2, 5))
print(2**5)
print(pow(2, 5))
print("-------------------------------")

# math.sqrt()
# Verilen sayının karekökünü hesaplar.
print(math.sqrt(16))
print("-------------------------------")

# math.degrees()
# Verilen sayıyı radyandan dereceye çevirir.
# math.radians()
# Verilen sayıyı dereceden radyana çevirir.
print(math.degrees(1.5707963267948966))
print(math.radians(180))
print("-------------------------------")

# math.sin()
# Radyan cinsinden verilen sayının sinüsünü hesaplar.
print(math.sin(math.radians(60)))
# math.cos()
# Radyan cinsinden verilen parametrenin kosinüsünü hesaplar.
# math.tan()
# Radyan cinsinden verilen parametrenin tanjantını hesaplar.
# math.cosh()
# Verilen değerin hiperbolik kosinüsünü döndürür.
print("-------------------------------")
