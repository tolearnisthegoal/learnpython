print("Enter TB or GB for the advertised unit:")
unit = input(">>>")

if unit == "TB" or unit == "tb" or unit == "tB" or unit == "Tb":
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb' or unit == 'Gb' or unit == 'gB':
    discrepancy = 1000000000 / 1073741824



print("Enter the advertised capacity:")
advertised_capacity = input('>>')
advertised_capacity = float(advertised_capacity)
# Calculate the real capacity, round it to the nearest hundredths,
# and convert it to a string so it can be concatenated:
real_capacity = str(round(advertised_capacity * discrepancy , 2))

print('The actual capacity is ' + real_capacity + ' ' + unit)



