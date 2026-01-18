# convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
cel=int(input("Enter temperature in Celsius: "))
fah=celsius_to_fahrenheit(cel)
print(f"{cel}°C is equal to {fah}°F")
# convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
fah2=int(input("Enter temperature in Fahrenheit: "))
cel2=fahrenheit_to_celsius(fah2)
print(f"{fah2}°F is equal to {cel2}°C")