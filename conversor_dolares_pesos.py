dollars = input("How many dollars do you have?: ")
dollars = float(dollars)
pesos_value = 0.00028
pesos = dollars / pesos_value
pesos = round(pesos, 1)
pesos = str(pesos)
print("You have $" + pesos + "pesos")