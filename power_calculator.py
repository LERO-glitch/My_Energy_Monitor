def read_current():
    import random
    simulated_current = random.uniform(0.1, 2.5)
    return simulated_current

voltage = 12
current = read_current()
power = voltage * current

print(f"Измеренный ток: {current:.2f} А")
print(f"Напряжение в сети: {voltage} В")
print(f"Потребляемая мощность: {power:.2f} Вт")