from itertools import islice

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0
current_budget = money_capital + salary
while spend <= current_budget:
    #Вычитание трат из текущего бюджета
    current_budget -= spend
    month += 1
    # Увеличение трат со второго месяца и увеличение бюджета на следующий месяц
    if month >= 1:
        spend += spend * increase
        current_budget += salary

print("Количество месяцев, которое можно протянуть без долгов:", month)
