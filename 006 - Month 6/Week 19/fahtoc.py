#! python3
# Simple Program that converts F to C

# Commented out farenheit because of redundancy. Could be ommitted or inputted for user verification
# fahrenheit = 98.6  # This would be the same as const int or #define in C
celcius = ((float(input("Enter the degrees in (f): ")) - 32) * 5) / 9
kelvin = celcius + 273.15

print(" Temp in (c) = : ", celcius)
print(" Temp in (K) = : ", kelvin)

