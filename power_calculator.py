def read_current():
    import random
    simulated_current = random.uniform(0.1, 2.5)
    return simulated_current

voltage = 220
current = float(input("Введите значение тока в Амперах: "))
power = voltage * current

print(f"При токе {current} А и напряжении {voltage} В")
print(f"Потребляемая мощность составляет: {power} Вт")