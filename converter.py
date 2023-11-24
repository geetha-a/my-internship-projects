def temperature_converter(value, source_unit, target_unit):
    if source_unit == "celsius" and target_unit == "fahrenheit":
        result = (value * 9/5) + 32
    elif source_unit == "fahrenheit" and target_unit == "celsius":
        result = (value - 32) * 5/9
    else:
        print("Invalid conversion: {} to {}".format(source_unit, target_unit))
        return

    print("{} {} is equal to {} {}".format(value, source_unit, result, target_unit))


def length_converter(value, source_unit, target_unit):
    if source_unit == "meters" and target_unit == "feet":
        result = value * 3.28084
    elif source_unit == "feet" and target_unit == "meters":
        result = value / 3.28084
    else:
        print("Invalid conversion: {} to {}".format(source_unit, target_unit))
        return

    print("{} {} is equal to {} {}".format(value, source_unit, result, target_unit))


def weight_converter(value, source_unit, target_unit):
    if source_unit == "kilograms" and target_unit == "pounds":
        result = value * 2.20462
    elif source_unit == "pounds" and target_unit == "kilograms":
        result = value / 2.20462
    else:
        print("Invalid conversion: {} to {}".format(source_unit, target_unit))
        return

    print("{} {} is equal to {} {}".format(value, source_unit, result, target_unit))


# Prompt the user for input
value = float(input("Enter the value to convert: "))
source_unit = input("Enter the source unit (Celsius, Fahrenheit, Meters, Feet, Kilograms, Pounds): ")
target_unit = input("Enter the target unit (Celsius, Fahrenheit, Meters, Feet, Kilograms, Pounds): ")

# Convert the value based on the chosen type of converter
if source_unit.lower() == "celsius" and target_unit.lower() == "fahrenheit":
    temperature_converter(value, source_unit, target_unit)
elif source_unit.lower() == "fahrenheit" and target_unit.lower() == "celsius":
    temperature_converter(value, source_unit, target_unit)
elif source_unit.lower() == "meters" and target_unit.lower() == "feet":
    length_converter(value, source_unit, target_unit)
elif source_unit.lower() == "feet" and target_unit.lower() == "meters":
    length_converter(value, source_unit, target_unit)
elif source_unit.lower() == "kilograms" and target_unit.lower() == "pounds":
    weight_converter(value, source_unit, target_unit)
elif source_unit.lower() == "pounds" and target_unit.lower() == "kilograms":
    weight_converter(value, source_unit, target_unit)
else:
    print("Unsupported conversion: {} to {}".format(source_unit, target_unit))





