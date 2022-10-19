salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

first_month = salary - spend
need_money -= first_month
for i in range(9):
    need_money -= salary - spend * (increase + 1) ** (i + 1)

print(round(need_money))
