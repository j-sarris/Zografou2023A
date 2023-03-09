ch = input("(C)elsius to Fahreneit or (F)ahreneit to Celsius?: ") 

if ch.lower() == "c":

    # convert Celsius degrees to Fahrenheit

    temp_cels = input("Give temperature in Celsius degrees: ")
    temp_fahr = float(temp_cels) * 1.8 + 32

    print(f"Temperature in Fahreneit degrees is: {temp_fahr}")

elif ch.lower() == "f":
    temp_fahr = input("Give temperature in Fahreneit degrees: ")
    temp_cels = (float(temp_fahr) - 32) * 5/9

    print(f"Temperature in Celsius degrees is: {temp_cels}")

# Modify as to convert the other way around 
# Degrees Fahrenheit to Celsius, subtract 32 and multiply by 5/9
# Ask the user for which conversion
