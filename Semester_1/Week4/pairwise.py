def pairwise_digits(number_a, number_b):
    out = []
    for a,b in zip(number_a,number_b):
        if a == b:
            out.append("1")
        else:
            out.append("0")
    return "".join(out)

print(pairwise_digits("1100","1010"))  
print(pairwise_digits("123100","13210"))          
