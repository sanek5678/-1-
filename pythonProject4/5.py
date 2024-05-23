rub = int(input())
kop = int(input())
pie = int(input())
price = rub * 100 + kop
summa = price * pie
price_rub = summa // 100
price_kop = summa % 100
print(price_rub, price_kop)
#формат ввода: 12 (enter), 50 (enter), 5 (enter)
#формат вывода: сначала рубли, потом копейки
