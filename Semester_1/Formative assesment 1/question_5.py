import re


def molecule_to_list(molecule):
    """converts a molecule to a list of tuples contain the atomic symbol 
        and the ammount contained in the molecule

    Args:
        molecule (str): a string of a molecule, e.g H2OCa

    Returns:
        list of tuples: retuns in the form of [(atomic symbol,ammount in the molecule)]
    """
    if not molecule.isalnum():
        return None
    for j, char in enumerate(molecule):
        if molecule[j-1].isnumeric() and char.islower():
            return None

    combined_list = re.findall(r'([A-Z][a-z]*)(\d*)', molecule)
    return [tuple((elem[0], int(elem[1]) if elem[1] else 1))
            for i, elem in enumerate(combined_list)]
