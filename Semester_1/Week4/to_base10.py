import numpy as np
def to_base10(binary):
    denary = 0
    factor = 2 ** np.arange(len(binary))[::-1]
    for f,b in zip(factor,binary):
        denary += f * int(b)
    return denary

print(to_base10("1001100"))