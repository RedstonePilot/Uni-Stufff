ATOMS = {
    'H': {'name': 'Hydrogen', 'weight': 1.00797},
    'He': {'name': 'Helium', 'weight': 4.00260},
    'C': {'name': 'Carbon', 'weight': 12.011},
    'N': {'name': 'Nitrogen', 'weight': 14.0067},
    'O': {'name': 'Oxygen', 'weight': 15.9994},
    'Ca': {'name': 'Calium', 'weight': 40.08}
}


def molar_mass(molecule):
    """Takes a moelcule and returns the atomic weight

    Args:
        molecule (list of tuples): takes a list of tuples in the form of (symbol,ammount)
        e.g [("C",2),("O",1)]       

    Returns:
        float: returns a float of the atomic weight
        None: if the list contains invalid atoms
    """
    mass = 0
    for element, quantity in molecule:
        if element not in ATOMS:
            return None
        mass += ATOMS[element]["weight"] * quantity

    return mass


print(molar_mass([('C', 1), ('H', 3),
      ('C', 1), ('O', 1), ('O', 1), ('H', 1)]))
