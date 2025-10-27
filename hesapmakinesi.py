# Hesap makinesi kodu

# Kullanıcıdan iki sayı ve bir işlem türü alın
sayi1 = float(input("Lütfen ilk sayıyı girin: "))
sayi2 = float(input("Lütfen ikinci sayıyı girin: "))
islem = input("Lütfen bir işlem türü girin (+, -, * veya /): ")

# İşlemi gerçekleştirin ve sonucu ekrana yazdırın
if islem == '+':
  print(sayi1 + sayi2)
elif islem == '-':
  print(sayi1 - sayi2)
elif islem == '*':
  print(sayi1 * sayi2)
elif islem == '/':
  print(sayi1 / sayi2)
else:
  print("Geçersiz işlem türü girdiniz.")

