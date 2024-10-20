salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
for month in range(1, months+1):
    if month == 1:
        money_capital += abs(salary - spend)
    elif month > 1:
        # Увеличение трат со второго месяца
        spend += spend * increase
        money_capital += abs(salary - spend)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))