x = int()
y = 0
while x >= 0:
    x = int(input(" Masukkan bilangan : "))
    if x > y:
        y = int(x)
    if x == 0:
        break
print('\nAngka terbesar adalah : ', y)