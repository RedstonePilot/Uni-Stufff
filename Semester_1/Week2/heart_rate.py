"""Write a function that takes the age (int) and rate (the heart rate as an int) as parameters and
prints a description of a person's training zone based on his or her age and training heart rate,
rate. The zone is determined by comparing rate with the person's maximum heart rate m: (table)
"""

def zone(age, rate):
        max_rate = 208 - 0.7*age
        ratio = rate/max_rate
        if  ratio >= 0.9:
            print("IT")
        elif ratio >= 0.7:
            print("TT")
        elif ratio >= 0.5:
            print("AT")
        else:
            print("CP")

zone(30,140)