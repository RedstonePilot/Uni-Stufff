"""Write a series of functions that convert weight, distance,
and liquid measurement fromImperial to Metric system. For example, to convert weight:"""

def check_int(*numbers):
    for number in numbers:
        try:
            int(number)
        except ValueError:
            return 0
        

def weight_imperial2metric(st,lb):
    if check_int(st,lb) == 0:
        return 0
    kg = 0
    kg += int(st) * 6.35
    kg += int(lb) / 2.2
    return round(kg,3)

def weight_metric2imperial(kg):
    if check_int(kg) == 0:
        return 0
    st = int(kg) / 6.35
    lb = (st % 1)* 14

    return int(st), int(lb)


def distance_imperial2metric(ft, inches):
    if check_int(ft,inches) == 0:
        return 0
    meters = 0
    meters += int(ft) / 3.281
    meters += int(inches) / 39.37
    return round(meters,3)

def distance_metric2imperial(m):
    if check_int(m) == 0:
        return 0
    ft = int(m) * 3.281
    inches = (ft % 1) * 12
    return int(ft), int(inches)

def volume_imperial2metric(gal):
    if check_int(gal) == 0:
        return 0
    litres  = int(gal) * 3.785
    return round(litres,3)



choice = input("Choose the conversion:\n1. Weight\n2. Distance\n3. Volume\n")
to_metric = input("Choose which way to go:\n1. Imperial to metric\n2. Metric to imperial\n")
if choice == "1":
    if to_metric == "1":
        stones = input("Enter number of stones: ")
        pounds = input("Enter number of pounds: ")
        if weight_imperial2metric(stones,pounds) != 0:
            print(f"{int(stones)} st and {int(pounds)} lb = {weight_imperial2metric(stones,pounds)} kg")
        else:
            print("Enter a whole number")

    else:
        kg = input("Enter the number of Kilograms: ")
        if weight_metric2imperial(kg) != 0:
            st,lb = weight_metric2imperial(kg)
            print(f"{int(kg)} kg = {st} st, {lb} lb")

elif choice == "2":
    if to_metric == "1":
        feet = input("Enter number of feet: ")
        inches = input("Enter number of inches: ")
        if distance_imperial2metric(feet,inches) != 0:
            print(f"{int(feet)} ft and {int(inches)} in = {distance_imperial2metric(feet,inches)} m")
        else:
            print("Enter a whole number")
    else:
        meters = input("Enter the number of Meters: ")
        if distance_metric2imperial(meters) != 0:
            ft,inches = distance_metric2imperial(meters)
            print(f"{int(meters)} m = {ft} ft, {inches} in")



elif choice == "3":
    gal = input("Enter number of gallons: ")
    if volume_imperial2metric(gal) != 0:
        print(f"{int(gal)} gal = {volume_imperial2metric(gal)} l")
    else:
        print("Enter a whole number")
else:
    print("Enter a valid choice")