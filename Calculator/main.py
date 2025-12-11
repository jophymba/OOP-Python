from calculator import Calculator

calculator = Calculator()

first = float(input("Zadej prvni cislo: "))
calculator.first = first

second = float(input("Zadej druhe cislo: "))
calculator.second = second

print(f"Soucet: {calculator.scitani()}")
print(f"Rozdil: {calculator.deleni()}")
print(f"Soucin: {calculator.nasobeni()}")
print(f"Podil: {calculator.deleni()}")